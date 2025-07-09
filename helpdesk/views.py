from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HelpVideo
from .forms import AppSelectForm, TopicSelectForm
import pandas as pd
import os
from django.conf import settings

@login_required
def home(request):
    apps = HelpVideo.objects.values_list('app_name', flat=True).distinct()
    return render(request, 'helpdesk/home.html', {'apps': apps})

@login_required
def app_detail(request, app_name):
    videos = HelpVideo.objects.filter(app_name=app_name)
    return render(request, 'helpdesk/app_detail.html', {'app_name': app_name, 'videos': videos})

@login_required
def yourguide(request):
    csv_path = os.path.join(settings.MEDIA_ROOT, 'yourguide.csv')
    df = pd.read_csv(csv_path)
    app_choices = sorted(df['app'].unique())
    selected_app = request.GET.get('app')
    selected_topic = request.GET.get('topic')
    topics = []
    experts = []
    expert_details = []
    if selected_app:
        topics = sorted(df[df['app'] == selected_app]['topic'].unique())
    if selected_app and selected_topic:
        row = df[(df['app'] == selected_app) & (df['topic'] == selected_topic)]
        if not row.empty:
            expert_cols = [col for col in df.columns if col not in ['app', 'topic']]
            experts = [col for col in expert_cols if str(row.iloc[0][col]).strip() == '1']
            # Load developer details from developers.csv
            dev_csv_path = os.path.join(settings.MEDIA_ROOT, 'developers.csv')
            if os.path.exists(dev_csv_path):
                dev_df = pd.read_csv(dev_csv_path)
                for expert in experts:
                    dev_info = dev_df[dev_df['name'] == expert]
                    if not dev_info.empty:
                        expert_details.append({
                            'name': expert,
                            'email': dev_info.iloc[0]['email'],
                            'working_time': dev_info.iloc[0]['working_time'],
                            'timezone': dev_info.iloc[0]['timezone'],
                            'experience': dev_info.iloc[0]['experience'],
                        })
    return render(request, 'helpdesk/yourguide.html', {
        'app_choices': app_choices,
        'topics': topics,
        'selected_app': selected_app,
        'selected_topic': selected_topic,
        'experts': experts,
        'expert_details': expert_details
    })
