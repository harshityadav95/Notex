"""Cloud learning-path previews, styled to extend the existing landing cards."""
from html import escape

PATHS = [
    {
        'id': 'cloudflare', 'name': 'Cloudflare', 'title': 'Cloudflare at the edge',
        'color': '#e5c7b2', 'label': 'EDGE & SERVERLESS',
        'points': ['Workers and serverless foundations', 'DNS, caching and the global network', 'R2, D1 and stateful applications'],
        'intro': 'Start with the network. Then bring your code, data, and applications closer to the people using them.',
        'topics': [
            ('Understand the edge', 'Trace a request through DNS, the network, and the cache.'),
            ('Build with Workers', 'Explore request handlers, bindings, and local development.'),
            ('Choose your storage', 'Get oriented with R2 object storage, D1, and Durable Objects.'),
            ('Connect the pieces', 'Follow an official tutorial from your first request to deployment.'),
        ],
        'docs': 'https://developers.cloudflare.com/resources/',
    },
    {
        'id': 'azure', 'name': 'Azure', 'title': 'Build with Azure',
        'color': '#bdcbdc', 'label': 'CLOUD FOUNDATIONS',
        'points': ['Compute, storage and cloud foundations', 'Identity and virtual networking', 'Deploy and observe your applications'],
        'intro': 'Build a mental model of the cloud, from your first resource group to the services that keep an application running.',
        'topics': [
            ('Learn the foundations', 'Explore subscriptions, resource groups, regions, and cloud concepts.'),
            ('Run your application', 'Compare virtual machines, App Service, and container hosting.'),
            ('Connect and protect', 'Get familiar with virtual networks, Microsoft Entra ID, and access control.'),
            ('Operate with confidence', 'Explore monitoring, deployment workflows, and cost management.'),
        ],
        'docs': 'https://learn.microsoft.com/en-us/training/azure/',
    },
    {
        'id': 'kubernetes', 'name': 'Kubernetes', 'title': 'Kubernetes in practice',
        'color': '#c9bdd7', 'label': 'CONTAINERS & CLUSTERS',
        'points': ['Pods, deployments and services', 'Networking, configuration and storage', 'Scale, roll out and troubleshoot'],
        'intro': 'Go from a container to a running system. Understand the objects, the control loop, and what happens inside a cluster.',
        'topics': [
            ('Meet the cluster', 'Understand nodes, the control plane, and the desired-state model.'),
            ('Deploy a workload', 'Work through Pods, Deployments, labels, and configuration.'),
            ('Expose and connect', 'Explore Services, service discovery, and persistent storage.'),
            ('Keep it running', 'Follow the official basics: inspect, scale, and update an application.'),
        ],
        'docs': 'https://kubernetes.io/docs/tutorials/kubernetes-basics/',
    },
]


def render():
    cards, dialogs = [], []
    for path in PATHS:
        key, name = path['id'], path['name']
        image = f'assets/cloud/{key}-notebook.png'
        points = ''.join(f'<li>{escape(point)}</li>' for point in path['points'])
        cards.append(f'''<article class="path-card cloud-card" style="--cloud-color:{path['color']}">
            <img class="cloud-art" src="{image}" alt="Illustrated {name} field notebook" width="800" height="800" loading="lazy">
            <h3>{path['title']}</h3><ul>{points}</ul>
            <span class="count">4 TOPICS · PATH PREVIEW</span>
            <button class="card-foot cloud-open" data-cloud-path="{key}" aria-haspopup="dialog" aria-controls="{key}-path" aria-label="Explore the {name} path">Explore path <span aria-hidden="true">→</span></button>
        </article>''')
        topics = ''.join(f'<li><h3>{title}</h3><p>{description}</p></li>' for title, description in path['topics'])
        dialogs.append(f'''<dialog class="cloud-dialog" id="{key}-path" aria-labelledby="{key}-title" aria-describedby="{key}-intro" style="--cloud-color:{path['color']}">
            <div class="cloud-dialog-head"><span class="eyebrow">{path['label']} / PATH PREVIEW</span><button class="tactile" aria-label="Close {name} preview" data-close autofocus>Close <span aria-hidden="true">×</span></button></div>
            <div class="cloud-dialog-layout"><div class="cloud-dialog-cover"><img src="{image}" alt="" width="800" height="800"></div>
            <div class="cloud-dialog-copy"><h2 id="{key}-title">{path['title']}</h2><p id="{key}-intro">{path['intro']}</p>
            <ol class="cloud-topics">{topics}</ol>
            <p class="cloud-preview-note">A starting map for your learning. Continue with the official guides and tutorials.</p>
            <a class="primary tactile" href="{path['docs']}" target="_blank" rel="noopener noreferrer">Open {name} guides <span aria-hidden="true">↗</span></a>
            </div></div>
        </dialog>''')
    return f'''<section class="cloud-section narrow" id="cloud" aria-labelledby="cloud-title">
        <p class="eyebrow">CLOUD & INFRASTRUCTURE</p><h2 id="cloud-title">From code to cloud</h2>
        <p class="cloud-intro">Build at the edge. Understand the cloud. Run your own cluster.</p>
        <div class="path-grid cloud-grid">{''.join(cards)}</div>
        <div class="cloud-section-foot"><span class="eyebrow">THREE PATHS. ONE CONNECTED STACK.</span><a href="Learning_System_Design/">Start with system design <span aria-hidden="true">↗</span></a></div>
    </section>{''.join(dialogs)}'''
