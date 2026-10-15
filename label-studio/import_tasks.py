"""Create the "Risk assessment answers" project in the local Label Studio and load tasks.json into it.

Run with the Label Studio environment, after you have signed up in the browser:

    LABEL_STUDIO_BASE_DATA_DIR=~/label-studio-local/data \
    ~/label-studio-local/venv/bin/python label-studio/import_tasks.py
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "label_studio.core.settings.label_studio")
os.environ.setdefault("LABEL_STUDIO_BASE_DATA_DIR", str(Path.home() / "label-studio-local" / "data"))

import django  # noqa: E402

django.setup()

from django.contrib.auth import get_user_model  # noqa: E402
from projects.models import Project  # noqa: E402
from tasks.models import Prediction, Task  # noqa: E402

TITLE = "Risk assessment answers"

user = get_user_model().objects.order_by("id").first()
if user is None:
    sys.exit("No Label Studio user yet. Sign up at http://localhost:8080 first, then run this again.")

config = (HERE / "label-config.xml").read_text()
tasks = json.loads((HERE / "tasks.json").read_text())

project = Project.objects.filter(title=TITLE, created_by=user).first()
if project is None:
    project = Project.objects.create(
        title=TITLE,
        description="Answers from the regulatory risk assessment form, one task per risk answer.",
        label_config=config,
        created_by=user,
        organization=user.active_organization,
    )
else:
    project.label_config = config
    project.save()

existing = set(Task.objects.filter(project=project).values_list("data__key", flat=True))
added = 0
for item in tasks:
    if item["data"]["key"] in existing:
        continue
    task = Task.objects.create(project=project, data=item["data"])
    for pred in item.get("predictions", []):
        Prediction.objects.create(task=task, project=project, result=pred["result"], model_version=pred["model_version"])
    added += 1

project.update_tasks_states(
    maximum_annotations_changed=False, overlap_cohort_percentage_changed=False, tasks_number_changed=True
)
print(f"Project {project.id} '{project.title}' for {user.email}: {added} tasks added, {len(existing)} already there.")
