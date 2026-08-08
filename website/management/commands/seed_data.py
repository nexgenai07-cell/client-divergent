# website/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from datetime import date

# Website app imports
from website.models import *
from blog.models import BlogPost
from projects.models import ProjectSection, ProjectCard
from about.models import AboutSection, TeamMember, Publication, Patent, AboutStat
from platformm.models import (
    PlatformSection, OperatingBenefit, WorkWithUs, ComingSoon,
    Demonstration, BuiltForProduction, PricingPlan
)


class Command(BaseCommand):
    help = 'Seed all website data for Divergent Physics'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('🌱 Starting to seed all data...'))

        # ============================================================
        # 1. WEBSITE APP DATA
        # ============================================================
        self.seed_website_data()
        
        # ============================================================
        # 2. BLOG APP DATA
        # ============================================================
        self.seed_blog_data()
        
        # ============================================================
        # 3. PROJECTS APP DATA
        # ============================================================
        self.seed_projects_data()
        
        # ============================================================
        # 4. ABOUT APP DATA
        # ============================================================
        self.seed_about_data()
        
        # ============================================================
        # 5. PLATFORM APP DATA
        # ============================================================
        self.seed_platform_data()

        self.stdout.write(self.style.SUCCESS('✅ All data seeded successfully!'))

    # ============================================================
    # SEED WEBSITE DATA
    # ============================================================
    def seed_website_data(self):
        self.stdout.write('  📦 Seeding website data...')

        # Hero Section
        hero, created = HeroSection.objects.get_or_create(
            title="AI Transformation for Simulation Engineering",
            defaults={
                'subtitle': "We design, build, and maintain AI agents that run your real workflows — CAD to simulation to customer-ready datasheet — inside the solver stack your team already uses.",
                'description': "Every workflow we encode becomes an asset you own — compounding as automation today, and as custom models trained on your own data next.",
                'built_by': "Built by PhDs in electromagnetics and applied mathematics who write automation code every day.",
                'call_to_action_1': "Book a Free Scoping Call →",
                'call_to_action_2': "Walk Through a Real Pilot",
                'is_active': True,
                'order': 1
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Hero Section'))

        # Pipeline Steps
        pipeline_data = [
            {'step_name': 'CAD', 'description': 'Your model, pulled straight from the CAD file you already have.', 'order': 1},
            {'step_name': 'SIMULATE', 'description': 'The agent runs the solver — setup, sweep, and optimization, unattended.', 'order': 2},
            {'step_name': 'VERIFY', 'description': 'Results checked against your spec before anything is called done.', 'order': 3},
            {'step_name': 'DATASHEET', 'description': 'A customer-ready report, generated automatically from the run.', 'order': 4},
        ]
        for data in pipeline_data:
            step, created = PipelineStep.objects.get_or_create(
                hero_section=hero,
                step_name=data['step_name'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Pipeline Step: {step.step_name}'))

        # Problem Statement
        problem, created = ProblemStatement.objects.get_or_create(
            heading="The Problem, in Engineers' Own Words",
            defaults={
                'sub_heading': "From 80+ interviews with RF and simulation engineers across aerospace, telecom, semiconductors, and medical devices.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Problem Statement'))

        # Problem Quotes
        quotes_data = [
            {
                'quote_text': 'I spent 3 hours manually fixing an asymmetric mesh — then gave up for the day.',
                'author': 'RF Engineer',
                'author_title': 'Medical-Device Startup',
                'order': 1
            },
            {
                'quote_text': 'Waiting 10 hours and then nothing. That\'s an entire day lost.',
                'author': 'Antenna Engineer',
                'author_title': 'Wireless Hardware Company',
                'order': 2
            },
            {
                'quote_text': 'A lot of the RF experts are baby boomers — we are going to lose a lot of these people.',
                'author': 'Engineering Leader',
                'author_title': 'Aerospace & Defense',
                'order': 3
            },
        ]
        for data in quotes_data:
            quote, created = ProblemQuote.objects.get_or_create(
                problem_statement=problem,
                quote_text=data['quote_text'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Problem Quote: {quote.author}'))

        # Statistics
        statistic, created = Statistic.objects.get_or_create(
            heading="AI | WEBSITE AI",
            defaults={
                'sub_heading': "From a production pilot with an antenna-in-package manufacturer — walk through it below ↓",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Statistics Section'))

        stats_data = [
            {'value': '1.5 h', 'label': 'Unattended run replacing an engineer-day of solver work', 'order': 1},
            {'value': '20+', 'label': 'Full-wave design candidates explored per run', 'order': 2},
            {'value': '0', 'label': 'Setups done by hand — agents do the clicking, engineers review the results', 'order': 3},
        ]
        for data in stats_data:
            stat, created = StatItem.objects.get_or_create(
                statistic=statistic,
                value=data['value'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Stat Item: {stat.value}'))

        # Field Notes
        field_note, created = FieldNote.objects.get_or_create(
            heading="The Problem in Engineers' Own Words",
            defaults={
                'sub_heading': "From 80+ interviews with RF and simulation engineers across aerospace, telecom, semiconductors, and medical devices.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Field Notes Section'))

        field_notes_data = [
            {
                'quote': 'I spent 3 hours manually fixing an asymmetric mesh — then gave up for the day.',
                'author': 'RF Engineer',
                'author_title': 'Medical-Device Startup',
                'order': 1
            },
            {
                'quote': 'Waiting 10 hours and then nothing. That\'s an entire day lost.',
                'author': 'Antenna Engineer',
                'author_title': 'Wireless Hardware Company',
                'order': 2
            },
            {
                'quote': 'A lot of the RF experts are baby boomers — we are going to lose a lot of these people.',
                'author': 'Engineering Leader',
                'author_title': 'Aerospace & Defense',
                'order': 3
            },
        ]
        for data in field_notes_data:
            note, created = FieldNoteItem.objects.get_or_create(
                field_note=field_note,
                quote=data['quote'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Field Note: {note.author}'))

        # Service Section
        service_section, created = ServiceSection.objects.get_or_create(
            heading="What We Do",
            defaults={
                'description': "End-to-end AI automation for simulation-driven engineering teams — done for you, or built with your engineers so your team owns it.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Service Section'))

        services_data = [
            {
                'heading': 'Agentic Workflow Development',
                'description': 'We take a workflow you already run — spec to simulation to report — and turn it into an AI agent that runs it end to end, unattended, with every step logged and reviewable.',
                'icon': 'fas fa-robot',
                'points': 'Automated geometry, meshing, and setup\nOptimization loops with verified results\nAuto-generated customer-facing reports',
                'order': 1
            },
            {
                'heading': 'Integration & Deployment',
                'description': 'AI automation deployed inside your solver environment and your security perimeter — tested, validated, and maintained as vendor releases ship.',
                'icon': 'fas fa-cloud-upload-alt',
                'points': 'Enterprise solver environment setup\nOn-premises or private deployment\nSecurity and compliance configuration',
                'order': 2
            },
        ]
        for data in services_data:
            service, created = ServiceCard.objects.get_or_create(
                service_section=service_section,
                heading=data['heading'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Service Card: {service.heading}'))

        # Case Study
        case_study, created = CaseStudy.objects.get_or_create(
            heading="Product ID In. Optimized Design and Datasheet Out.",
            defaults={
                'description': "A manufacturer of configurable antenna-in-package modules needed every customer configuration verified, optimized, and documented in Ansys HFSS — an engineer-day of expert work per part. We encoded their process as an agent-run workflow.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Case Study'))

        case_study_data = [
            {
                'title': 'The workflow became a skill — data, not code',
                'description': "Their engineers' process, written once as a reviewable document the agent follows: load the right catalog model, set targets from the customer spec, optimize only within manufacturer-approved bounds, verify the winner, and generate the datasheet.",
                'order': 1
            },
            {
                'title': 'One unattended run, end to end',
                'description': 'Baseline solve, KPI check against spec, Bayesian optimization over approved parameters, re-solve of the winning candidate, and a customer-facing datasheet — patterns, gain, matching, efficiency — with zero hand-editing.',
                'order': 2
            },
        ]
        for data in case_study_data:
            card, created = CaseStudyCard.objects.get_or_create(
                case_study=case_study,
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Case Study Card: {card.title}'))

        # Asset Section
        asset_section, created = AssetSection.objects.get_or_create(
            heading="Key Assets & Capabilities",
            defaults={
                'description': "Our platform provides comprehensive automation capabilities for simulation engineering teams.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Asset Section'))

        assets_data = [
            {
                'title': 'Agentic Workflow Automation',
                'description': 'End-to-end automation of simulation workflows from CAD to datasheet.',
                'order': 1
            },
            {
                'title': 'Custom AI Model Training',
                'description': 'Train proprietary models on your simulation data for instant predictions.',
                'order': 2
            },
            {
                'title': 'Enterprise Integration',
                'description': 'Seamless integration with existing solvers and enterprise systems.',
                'order': 3
            },
        ]
        for data in assets_data:
            asset, created = AssetItem.objects.get_or_create(
                asset_section=asset_section,
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Asset Item: {asset.title}'))

        # How We Work
        how_we_work, created = HowWeWork.objects.get_or_create(
            heading="How We Work",
            defaults={
                'description': "Your team keeps operating normally throughout — about an hour of engineer time per week during a pilot. Agents do the clicking; your engineers review the results.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created How We Work Section'))

        steps_data = [
            {
                'step_number': 1,
                'title': 'Discovery',
                'description': 'Walk us through one workflow — a 30-minute screen share of the work your engineers repeat most. We tell you on the spot whether it\'s automatable, what a pilot looks like, and what it would cost.',
                'order': 1
            },
            {
                'step_number': 2,
                'title': 'Pilot',
                'description': 'We embed with your team and encode one workflow you already run — weekly working sessions, about an hour of your engineers\' time per week. You judge the results against your own acceptance criteria.',
                'order': 2
            },
            {
                'step_number': 3,
                'title': 'Deploy',
                'description': 'The automation moves into your environment — your security perimeter, your solvers, your data — with testing and validation before anything touches production work.',
                'order': 3
            },
            {
                'step_number': 4,
                'title': 'Scale & Support',
                'description': 'From one workflow to a fleet: engineers set direction and review while agents fan out across products, specs, and what-if studies. We maintain as your solvers evolve.',
                'order': 4
            },
        ]
        for data in steps_data:
            step, created = HowWeWorkStep.objects.get_or_create(
                how_we_work=how_we_work,
                step_number=data['step_number'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created How We Work Step: {step.title}'))

        # Why Us
        why_us, created = WhyUsSection.objects.get_or_create(
            heading="Why Divergent Physics",
            defaults={'is_active': True}
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Why Us Section'))

        why_us_data = [
            {
                'number': '01',
                'title': 'Engineers, Not Career Consultants',
                'description': 'Founded by three PhDs in electromagnetics and applied mathematics, with industry experience at companies including Apple and Ansys. The people on the call are the people in the code.',
                'order': 1
            },
            {
                'number': '02',
                'title': 'Trusted in Production',
                'description': 'Beyond the pilot above, we are delivering a milestone-gated automation program for the RF systems team of a Fortune-100 consumer-electronics manufacturer — invoiced against acceptance criteria, not hours.',
                'order': 2
            },
        ]
        for data in why_us_data:
            card, created = WhyUsCard.objects.get_or_create(
                why_us_section=why_us,
                number=data['number'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Why Us Card: {card.title}'))

        # Our Platform
        platform, created = OurPlatform.objects.get_or_create(
            heading="Built on Our Own Platform",
            defaults={
                'description': "Every engagement is delivered on the agent platform we build and maintain — the RF and EM understanding layer that turns a request into a correct simulation.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Our Platform Section'))

        platform_features = [
            {
                'title': 'HFSS Agent',
                'description': 'AI agents that understand RF and electromagnetics, turning natural language requests into correct simulations.',
                'order': 1
            },
            {
                'title': 'Agent Chat',
                'description': 'Compare S11 across design variations using natural language commands against live HFSS projects.',
                'order': 2
            },
            {
                'title': 'Notebook Integration',
                'description': 'Seamless integration with Jupyter notebooks for analysis, visualization, and reporting.',
                'order': 3
            },
        ]
        for data in platform_features:
            feature, created = PlatformFeature.objects.get_or_create(
                platform=platform,
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Platform Feature: {feature.title}'))

        # FAQs
        faqs_data = [
            {
                'question': 'What is Divergent Physics?',
                'answer': 'Divergent Physics builds AI agents that automate physics-based simulation end-to-end — from antenna design in Ansys HFSS to complete wireless systems.',
                'order': 1
            },
            {
                'question': 'What solvers do you support?',
                'answer': 'We currently support Ansys HFSS with full integration. CST and other solvers are coming soon.',
                'order': 2
            },
            {
                'question': 'How long does a pilot take?',
                'answer': 'A typical pilot runs for 4-6 weeks with about an hour of your engineers\' time per week.',
                'order': 3
            },
            {
                'question': 'Is my data secure?',
                'answer': 'Yes. All automation runs inside your secure environment with enterprise encryption and isolated compute.',
                'order': 4
            },
        ]
        for data in faqs_data:
            faq, created = FAQ.objects.get_or_create(
                question=data['question'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created FAQ: {faq.question[:30]}...'))

        # Get Started
        get_started, created = GetStartedSection.objects.get_or_create(
            heading="Get Started with AI-Powered Simulation",
            defaults={
                'description': "Transform your engineering workflow today. Let's discuss how we can help you automate your simulation processes.",
                'call_to_action': "Book a Consultation →",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Get Started Section'))

        self.stdout.write(self.style.SUCCESS('  ✅ Website data seeded!'))

    # ============================================================
    # SEED BLOG DATA
    # ============================================================
    def seed_blog_data(self):
        self.stdout.write('  📦 Seeding blog data...')

        blog_posts = [
            {
                'title': 'AI Automation in Simulation Engineering',
                'description': 'How AI agents are transforming the way engineers approach simulation workflows.',
                'content': 'Full content goes here. AI agents are revolutionizing simulation engineering by automating repetitive tasks and enabling engineers to focus on high-value design decisions.',
                'author': 'Dr. Sarah Chen',
                'read_time': '5 min read',
                'published_date': date(2024, 1, 15),
                'order': 1,
                'is_active': True
            },
            {
                'title': 'Bayesian Optimization for Ansys HFSS',
                'description': 'Using Bayesian optimization to reduce simulation time while finding optimal designs.',
                'content': 'Full content goes here. Bayesian optimization provides a systematic approach to finding optimal designs while minimizing the number of expensive simulation runs.',
                'author': 'Dr. James Wilson',
                'read_time': '7 min read',
                'published_date': date(2024, 1, 10),
                'order': 2,
                'is_active': True
            },
            {
                'title': 'How AI is Reshaping Electromagnetic Simulation',
                'description': 'Exploring the intersection of artificial intelligence and electromagnetic field simulation.',
                'content': 'Full content goes here. AI is reshaping electromagnetic simulation by enabling faster predictions, automated workflows, and intelligent design exploration.',
                'author': 'Prof. Michael Roberts',
                'read_time': '8 min read',
                'published_date': date(2024, 1, 5),
                'order': 3,
                'is_active': True
            },
        ]

        for post_data in blog_posts:
            # Generate slug from title
            post_data['slug'] = slugify(post_data['title'])
            
            post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults=post_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Blog Post: {post.title}'))

        self.stdout.write(self.style.SUCCESS('  ✅ Blog data seeded!'))

    # ============================================================
    # SEED PROJECTS DATA
    # ============================================================
    def seed_projects_data(self):
        self.stdout.write('  📦 Seeding projects data...')

        # Project Section
        section, created = ProjectSection.objects.get_or_create(
            heading="Case Studies & Projects",
            defaults={
                'description': "Real-world implementations of AI automation for simulation engineering.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Project Section'))

        projects_data = [
            {
                'number': '01',
                'heading': 'Antenna-in-Package Optimization',
                'description': 'Automated HFSS workflow for configurable antenna modules, reducing setup time from days to 1.5 hours unattended.',
                'icon': 'fas fa-satellite-dish',
                'points': 'Automated geometry, meshing, and setup\nOptimization loops with verified results\nAuto-generated customer-facing reports',
                'technologies': 'Ansys HFSS\nPython\nBayesian Optimization\nAI Agents',
                'key_results': '1.5 hours unattended run time\n90% reduction in manual setup\n20+ design candidates explored per run\nFull audit trail with replayable runs',
                'order': 1
            },
            {
                'number': '02',
                'heading': 'Fortune-100 Consumer Electronics',
                'description': 'Milestone-gated automation program for RF systems team, delivering verified simulation workflows with acceptance criteria.',
                'icon': 'fas fa-microchip',
                'points': 'Enterprise solver environment setup\nOn-premises or private deployment\nSecurity and compliance configuration',
                'technologies': 'RF Systems\nEnterprise Integration\nAutomation',
                'key_results': 'Milestone-gated delivery\nVerified simulation workflows\nEnterprise-grade integration\nAcceptance criteria based invoicing',
                'order': 2
            },
            {
                'number': '03',
                'heading': 'Aerospace Radar Simulation',
                'description': 'AI-powered radar simulation automation for aerospace defense systems, reducing simulation time by 70%.',
                'icon': 'fas fa-rocket',
                'points': 'Complex geometry handling\nMulti-frequency sweep automation\nAutomated report generation',
                'technologies': 'Ansys HFSS\nPython\nMachine Learning\nRadar Systems',
                'key_results': '70% reduction in simulation time\n100% automated report generation\nZero manual interventions',
                'order': 3
            },
        ]

        for data in projects_data:
            project, created = ProjectCard.objects.get_or_create(
                project_section=section,
                heading=data['heading'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Project: {project.heading}'))

        self.stdout.write(self.style.SUCCESS('  ✅ Projects data seeded!'))

    # ============================================================
    # SEED ABOUT DATA
    # ============================================================
    def seed_about_data(self):
        self.stdout.write('  📦 Seeding about data...')

        # About Section
        section, created = AboutSection.objects.get_or_create(
            heading="About Divergent Physics",
            defaults={
                'description': "Making physics-based simulation as simple as describing the problem. Divergent Physics builds AI agents that automate physics-based simulation end-to-end — from antenna design in Ansys HFSS to complete wireless systems. We pair deep RF and information-theory expertise with modern AI so engineering teams can move from idea to result without the manual setup.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created About Section'))

        # Stats
        stats_data = [
            {'label': 'Team Members', 'value': '3+', 'icon': 'fas fa-users', 'order': 1},
            {'label': 'Publications', 'value': '12', 'icon': 'fas fa-book', 'order': 2},
            {'label': 'Patents', 'value': '5', 'icon': 'fas fa-file-patent', 'order': 3},
            {'label': 'Years Experience', 'value': '20+', 'icon': 'fas fa-calendar-check', 'order': 4},
        ]
        for data in stats_data:
            stat, created = AboutStat.objects.get_or_create(
                about_section=section,
                label=data['label'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created About Stat: {stat.label}'))

        # Team Members
        team_data = [
            {
                'name': 'Dr. Sarah Chen',
                'designation': 'PhD, RF Engineering',
                'role': 'Co-Founder & CTO',
                'description': 'Former Apple RF engineer with 10+ years in antenna design and electromagnetics. Specializes in AI-driven optimization for wireless systems.',
                'linkedin': 'https://linkedin.com/in/sarahchen',
                'github': 'https://github.com/sarahchen',
                'order': 1
            },
            {
                'name': 'Dr. James Wilson',
                'designation': 'PhD, Applied Mathematics',
                'role': 'Co-Founder & Head of AI',
                'description': 'Former Ansys researcher with expertise in Bayesian optimization and surrogate modeling. Leads AI agent development for simulation automation.',
                'linkedin': 'https://linkedin.com/in/jameswilson',
                'github': 'https://github.com/jameswilson',
                'order': 2
            },
            {
                'name': 'Dr. Michael Roberts',
                'designation': 'PhD, Electromagnetics',
                'role': 'Co-Founder & Principal Engineer',
                'description': 'Expert in computational electromagnetics with background in defense and aerospace. Focuses on HFSS automation and solver integration.',
                'linkedin': 'https://linkedin.com/in/michaelroberts',
                'github': 'https://github.com/michaelroberts',
                'order': 3
            },
        ]
        for data in team_data:
            member, created = TeamMember.objects.get_or_create(
                about_section=section,
                name=data['name'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Team Member: {member.name}'))

        # Publications
        publications_data = [
            {
                'title': 'AI-Driven Optimization of Antenna Arrays Using Bayesian Methods',
                'authors': 'Chen, S., Wilson, J., Roberts, M.',
                'journal': 'IEEE Transactions on Antennas and Propagation',
                'year': 2024,
                'link': 'https://doi.org/10.1109/TAP.2024.123456',
                'citation': 'Chen, S., Wilson, J., & Roberts, M. (2024). AI-Driven Optimization of Antenna Arrays Using Bayesian Methods. IEEE Transactions on Antennas and Propagation, 72(1), 123-135.',
                'order': 1
            },
            {
                'title': 'Surrogate-Assisted Simulation for Rapid Electromagnetic Design',
                'authors': 'Wilson, J., Chen, S., Roberts, M.',
                'journal': 'Journal of Computational Physics',
                'year': 2023,
                'link': 'https://doi.org/10.1016/j.jcp.2023.112345',
                'citation': 'Wilson, J., Chen, S., & Roberts, M. (2023). Surrogate-Assisted Simulation for Rapid Electromagnetic Design. Journal of Computational Physics, 456, 112345.',
                'order': 2
            },
            {
                'title': 'Automated Workflow for Antenna-in-Package Design Using AI Agents',
                'authors': 'Roberts, M., Chen, S., Wilson, J.',
                'journal': 'IEEE Antennas and Wireless Propagation Letters',
                'year': 2024,
                'link': 'https://doi.org/10.1109/LAWP.2024.123457',
                'citation': 'Roberts, M., Chen, S., & Wilson, J. (2024). Automated Workflow for Antenna-in-Package Design Using AI Agents. IEEE Antennas and Wireless Propagation Letters, 23(2), 456-460.',
                'order': 3
            },
        ]
        for data in publications_data:
            pub, created = Publication.objects.get_or_create(
                about_section=section,
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Publication: {pub.title[:30]}...'))

        # Patents
        patents_data = [
            {
                'title': 'System and Method for AI-Driven Simulation Optimization',
                'patent_number': 'US 11,123,456 B2',
                'inventors': 'Chen, S., Wilson, J., Roberts, M.',
                'year': 2024,
                'link': 'https://patents.google.com/patent/US11123456B2/',
                'order': 1
            },
            {
                'title': 'Automated Antenna Design Using Machine Learning',
                'patent_number': 'US 11,234,567 B2',
                'inventors': 'Wilson, J., Chen, S., Roberts, M.',
                'year': 2023,
                'link': 'https://patents.google.com/patent/US11234567B2/',
                'order': 2
            },
        ]
        for data in patents_data:
            patent, created = Patent.objects.get_or_create(
                about_section=section,
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Patent: {patent.title[:30]}...'))

        self.stdout.write(self.style.SUCCESS('  ✅ About data seeded!'))

    # ============================================================
    # SEED PLATFORM DATA
    # ============================================================
    def seed_platform_data(self):
        self.stdout.write('  📦 Seeding platform data...')

        # Platform Section
        section, created = PlatformSection.objects.get_or_create(
            heading="Built for Enterprise Simulation Workflows",
            defaults={
                'description': "Scale simulation impact without increasing headcount. Deploy AI agents across your solvers and accelerate design iteration.",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Platform Section'))

        # Operating Benefits
        benefits_data = [
            {
                'heading': 'Deploy AI Agents Across Your Solvers',
                'description': 'Automate repetitive tasks across your simulation workflow — from CAD to insights report — so engineers can focus on high-value design decisions.',
                'impact': 'Accelerate post-processing and design iteration',
                'icon': 'fas fa-robot',
                'order': 1
            },
            {
                'heading': 'Parallel Scenario Exploration',
                'description': 'Run multiple design variations simultaneously across solver instances. Compare antenna performance and optimize matching networks more efficiently.',
                'impact': 'Faster evaluation of design alternatives',
                'icon': 'fas fa-layer-group',
                'order': 2
            },
            {
                'heading': 'No Migration Required',
                'description': 'Enhance your existing solver workflows with AI automation — no retraining or process changes required.',
                'impact': 'Immediate value with zero migration risk',
                'icon': 'fas fa-arrow-right',
                'order': 3
            },
        ]
        for data in benefits_data:
            benefit, created = OperatingBenefit.objects.get_or_create(
                platform_section=section,
                heading=data['heading'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Operating Benefit: {benefit.heading}'))

        # Work With Us
        work_data = [
            {
                'heading': 'Two Ways to Work With Us',
                'description': 'Run the agents yourself, or have our team build the automation for you. Either way, you get the same RF and EM understanding layer — maintained against every solver release.',
                'title': 'Agents',
                'icon': 'fas fa-microchip',
                'cta_label': 'Start Free Trial',
                'cta_link': '/trial',
                'order': 1
            },
            {
                'heading': '',
                'description': 'Self-serve AI agents that run your EM simulations across solvers, built on our domain understanding layer and kept current with every solver release. HFSS today; CST coming soon.',
                'title': 'Services',
                'icon': 'fas fa-concierge-bell',
                'cta_label': 'Explore Services',
                'cta_link': '/services',
                'order': 2
            },
        ]
        for data in work_data:
            work, created = WorkWithUs.objects.get_or_create(
                platform_section=section,
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Work With Us: {work.title}'))

        # Coming Soon
        coming_soon_data = [
            {
                'heading': 'Turn Your Simulation Data Into Custom AI Models',
                'description': 'Your team runs thousands of simulations. Divergent Physics helps you train proprietary AI models on that data — so you can predict performance in seconds instead of hours.',
                'title': 'Your Data, Your Models',
                'icon': 'fas fa-database',
                'order': 1
            },
            {
                'heading': '',
                'description': 'Train AI surrogate models on your proprietary CAE and simulation datasets. Get near-instant predictions for design parameters that currently require full simulation runs.',
                'title': 'Accelerate Design Exploration',
                'icon': 'fas fa-rocket',
                'order': 2
            },
            {
                'heading': '',
                'description': 'Models are trained and deployed within your secure environment. Your proprietary simulation data and trained models never leave your infrastructure.',
                'title': 'Enterprise-Grade & Secure',
                'icon': 'fas fa-shield-alt',
                'order': 3
            },
        ]
        for data in coming_soon_data:
            cs, created = ComingSoon.objects.get_or_create(
                platform_section=section,
                title=data['title'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Coming Soon: {cs.title}'))

        # Demonstration
        demo, created = Demonstration.objects.get_or_create(
            platform_section=section,
            heading="See Divergent Physics in Action",
            defaults={
                'description': 'See how teams democratize simulation expertise and ship designs faster. Junior engineers create simulation-ready geometries in seconds with natural language — automated defeating strips unnecessary CAD details so models are simulation-ready without manual cleanup.',
                'cta_label': 'Book a Consultation →',
                'cta_link': '/contact',
                'order': 1,
                'is_active': True
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'    ✅ Created Demonstration'))

        # Built For Production
        production_data = [
            {
                'heading': 'IP Protection & Data Security',
                'description': 'Runs inside your secure environment, with support for enterprise encryption and isolated compute.',
                'icon': 'fas fa-lock',
                'order': 1
            },
            {
                'heading': 'Solver-Native Integration',
                'description': 'Uses official vendor APIs and licensing — Ansys HFSS today, Dassault CST next — to ensure compatibility without hacks or reverse engineering.',
                'icon': 'fas fa-plug',
                'order': 2
            },
            {
                'heading': 'Maintained Against Every Release',
                'description': 'We track solver version drift and the PyAEDT integration quirks so your automation keeps working release after release — the maintenance burden that sinks internal builds, carried by us.',
                'icon': 'fas fa-sync-alt',
                'order': 3
            },
        ]
        for data in production_data:
            prod, created = BuiltForProduction.objects.get_or_create(
                platform_section=section,
                heading=data['heading'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Built For Production: {prod.heading}'))

        # Pricing Plans
        pricing_data = [
            {
                'name': 'Professional',
                'price': '$400 PER MONTH',
                'description': 'Access to core simulation agents (Ansys HFSS today; CST coming soon)',
                'what_included': 'Access to core simulation agents (Ansys HFSS today; CST coming soon)\nAutomated post-processing (plotting, reporting, beam steering, sidelobe control, etc.)\nUnlimited projects & saved configurations',
                'best_for': 'Individuals & Small Teams',
                'cta_label': 'Start Free Trial',
                'cta_link': '/trial',
                'is_featured': False,
                'order': 1
            },
            {
                'name': 'Enterprise',
                'price': 'Custom Pricing',
                'description': 'Everything in Professional plus custom workflow development and enterprise integration.',
                'what_included': 'Everything in Professional\nA complete agentic workflow set up for your RF/EM simulation\nIntegration with your existing solvers, CAD/PLM, and pipelines\nCustom workflow development & automation, built for your team',
                'best_for': 'Enterprise Teams & Organizations',
                'cta_label': 'Book a Consultation →',
                'cta_link': '/contact',
                'is_featured': True,
                'order': 2
            },
        ]
        for data in pricing_data:
            plan, created = PricingPlan.objects.get_or_create(
                platform_section=section,
                name=data['name'],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'    ✅ Created Pricing Plan: {plan.name}'))

        self.stdout.write(self.style.SUCCESS('  ✅ Platform data seeded!'))