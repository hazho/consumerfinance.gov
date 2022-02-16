# Generated by Django 2.2.27 on 2022-02-16 19:29

from django.db import migrations, models
import django.db.models.deletion
import v1.models.filterable_list_mixins


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0278_remove_unused_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchHubPage',
            fields=[
                ('sublandingfilterablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='v1.SublandingFilterablePage')),
            ],
            options={
                'abstract': False,
            },
            bases=(v1.models.filterable_list_mixins.CategoryFilterableMixin, 'v1.sublandingfilterablepage'),
        ),
        migrations.AlterField(
            model_name='cfgovpagecategory',
            name='name',
            field=models.CharField(choices=[('Administrative adjudication docket', (('administrative-adjudication', 'Administrative adjudication'), ('stipulation-and-constent-order', 'Stipulation and consent order'))), ('Amicus Brief', (('us-supreme-court', 'U.S. Supreme Court'), ('fed-circuit-court', 'Federal Circuit Court'), ('fed-district-court', 'Federal District Court'), ('state-court', 'State Court'))), ('Blog', (('at-the-cfpb', 'At the CFPB'), ('directors-notebook', "Director's notebook"), ('policy_compliance', 'Policy and compliance'), ('data-research-reports', 'Data, research, and reports'), ('info-for-consumers', 'Info for consumers'))), ('Consumer Reporting Companies', (('nationwide', 'Nationwide'), ('employment-screening', 'Employment screening'), ('tenant-screening', 'Tenant screening'), ('check-bank-screening', 'Check and bank screening'), ('personal-property-insurance', 'Personal property insurance'), ('medical', 'Medical'), ('low-income-and-subprime', 'Low-income and subprime'), ('supplementary-reports', 'Supplementary reports'), ('utilities', 'Utilities'), ('retail', 'Retail'), ('gaming', 'Gaming'))), ('Enforcement Action', (('administrative-proceeding', 'Administrative Proceeding'), ('civil-action', 'Civil Action'))), ('Final rule', (('interim-final-rule', 'Interim final rule'), ('final-rule', 'Final rule'))), ('FOIA Frequently Requested Record', (('report', 'Report'), ('log', 'Log'), ('record', 'Record'))), ('Newsroom', (('consumer-advisories', 'Consumer advisories'), ('directors-statement', "Director's statement"), ('op-ed', 'Op-ed'), ('press-release', 'Press release'), ('speech', 'Speech'), ('testimony', 'Testimony'))), ('Notice and Opportunity for Comment', (('notice-proposed-rule', 'Advance notice of proposed rulemaking'), ('proposed-rule', 'Proposed rule'), ('interim-final-rule-2', 'Interim final rule'), ('request-comment-info', 'Request for comment or information'), ('proposed-policy', 'Proposed policy'), ('intent-preempt-determ', 'Intent to make preemption determination'), ('info-collect-activity', 'Information collection activities'), ('notice-privacy-act', 'Notice related to Privacy Act'))), ('Research Hub', (('data-point', 'Data point'), ('industry-markets', 'Industry and markets'))), ('Research Report', (('consumer-complaint', 'Consumer complaint'), ('super-highlight', 'Supervisory Highlights'), ('data-point', 'Data point'), ('industry-markets', 'Industry and markets'), ('consumer-edu-empower', 'Consumer education and empowerment'), ('to-congress', 'To Congress'))), ('Rule Under Development', (('notice-proposed-rule-2', 'Advance notice of proposed rulemaking'), ('proposed-rule-2', 'Proposed rule'))), ('Story', (('auto-loans', 'Auto loans'), ('bank-accts-services', 'Bank accounts and services'), ('credit-cards', 'Credit cards'), ('credit-reports-scores', 'Credit reports and scores'), ('debt-collection', 'Debt collection'), ('money-transfers', 'Money transfers'), ('mortgages', 'Mortgages'), ('payday-loans', 'Payday loans'), ('prepaid-cards', 'Prepaid cards'), ('student-loans', 'Student loans')))], max_length=255),
        ),
    ]
