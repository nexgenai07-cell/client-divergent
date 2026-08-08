from django.core.management.base import BaseCommand
from website.models import Page, Section, SectionItem, NavLink, PricingPlan, SiteSettings
from blog.models import BlogPost


class Command(BaseCommand):
    help = 'Seeds sample data into all models'

    def handle(self, *args, **kwargs):
        # ---------------- SiteSettings ----------------
        settings_obj = SiteSettings.load()
        settings_obj.site_name = "Divergence Demo"
        settings_obj.calendar_link = "https://calendly.com/example/consultation"
        settings_obj.copyright_text = "© 2026 Divergence Demo. All rights reserved."
        settings_obj.social_links = {"linkedin": "https://linkedin.com/company/example", "twitter": "https://x.com/example"}
        settings_obj.save()
        self.stdout.write(self.style.SUCCESS('SiteSettings seeded'))

        # ---------------- NavLinks ----------------
        nav_items = [
            ("Services", "/services", "nav", 1),
            ("Case Study", "/case-study", "nav", 2),
            ("How We Work", "/how-we-work", "nav", 3),
            ("Wireless", "/wireless", "nav", 4),
            ("About", "/about", "nav", 5),
            ("Blog", "/blog", "nav", 6),
            ("Privacy Policy", "/privacy", "footer", 1),
            ("Terms of Service", "/terms", "footer", 2),
        ]
        for label, link, location, order in nav_items:
            NavLink.objects.get_or_create(label=label, location=location, defaults={"link": link, "order": order})
        self.stdout.write(self.style.SUCCESS('NavLinks seeded'))

        # ================= HOME PAGE =================
        home, _ = Page.objects.get_or_create(
            name="home",
            defaults={"title": "Home", "meta_description": "AI automation for engineering workflows", "order": 1}
        )

        # Hero
        Section.objects.get_or_create(
            page=home, section_type="hero",
            defaults={
                "name": "Main Hero",
                "heading": "AI Transformation for Simulation Engineering",
                "subheading": "We turn repetitive engineering workflows into autonomous AI agents.",
                "button_text": "Book a Call",
                "button_link": "/contact",
                "order": 1,
            }
        )

        # Problem
        problem, _ = Section.objects.get_or_create(
            page=home, section_type="problem",
            defaults={
                "name": "Problem Framing",
                "heading": "The bottleneck isn't compute, it's manual work",
                "subheading": "Engineering teams lose weeks to repetitive simulation setup.",
                "order": 2,
            }
        )
        problem_cards = [
            ("Mesh Fixing Takes Days", "Engineers spend hours manually correcting mesh errors before every run."),
            ("Expertise Is Trapped", "Senior engineers' knowledge lives in their heads, not in reusable systems."),
            ("Long Solver Wait Times", "Teams idle while simulations run instead of working on the next design."),
        ]
        for i, (title, desc) in enumerate(problem_cards, start=1):
            SectionItem.objects.get_or_create(section=problem, title=title, defaults={"description": desc, "order": i})

        # Stats
        stats, _ = Section.objects.get_or_create(
            page=home, section_type="stats",
            defaults={"name": "Impact Stats", "heading": "Results That Matter", "order": 3}
        )
        stat_items = [
            ("80%", "Reduction in manual setup time"),
            ("3x", "Faster design iteration cycles"),
            ("24/7", "Unattended simulation runs"),
        ]
        for i, (title, desc) in enumerate(stat_items, start=1):
            SectionItem.objects.get_or_create(section=stats, title=title, defaults={"description": desc, "order": i})

        # Field Notes (testimonials / quotes from engineers)
        field_notes, _ = Section.objects.get_or_create(
            page=home, section_type="field_notes",
            defaults={"name": "Field Notes", "heading": "What Engineers Told Us", "order": 4}
        )
        notes = [
            ("The mesh cleanup alone eats a full day every time.", "Senior RF Engineer", "Antenna Manufacturer"),
            ("Our best people spend more time babysitting solvers than designing.", "Simulation Lead", "Defense Contractor"),
            ("Knowledge walks out the door every time someone retires.", "Engineering Director", "Telecom OEM"),
        ]
        for i, (quote, name, role) in enumerate(notes, start=1):
            SectionItem.objects.get_or_create(
                section=field_notes, title=quote,
                defaults={"name": name, "role": role, "order": i}
            )

        # Services
        services, _ = Section.objects.get_or_create(
            page=home, section_type="services",
            defaults={"name": "Our Services", "heading": "What We Do",
                      "subheading": "End-to-end support from discovery to deployment.", "order": 5}
        )
        service_items = [
            ("Agentic Workflow Development", "We build AI agents tailored to your simulation pipeline."),
            ("Integration & Deployment", "Seamless integration with your existing solver and CAD tools."),
            ("AI Enablement for Engineering Teams", "Training and tooling so your team can extend the agents."),
            ("Dedicated RF & EM Engineering", "Direct access to our in-house electromagnetics engineers."),
        ]
        for i, (title, desc) in enumerate(service_items, start=1):
            SectionItem.objects.get_or_create(section=services, title=title, defaults={"description": desc, "order": i})

        # Case Study
        case_study, _ = Section.objects.get_or_create(
            page=home, section_type="case_study",
            defaults={
                "name": "Case Study",
                "heading": "Antenna-in-Package Manufacturer",
                "subheading": "How we cut simulation turnaround from weeks to hours.",
                "order": 6,
            }
        )
        case_points = [
            ("Workflow as a Skill", "We captured the engineer's exact process as a reusable agent skill."),
            ("Unattended Optimization", "The agent ran overnight optimization loops without supervision."),
            ("Full Audit Trail", "Every run is logged and traceable back to the input parameters."),
        ]
        for i, (title, desc) in enumerate(case_points, start=1):
            SectionItem.objects.get_or_create(section=case_study, title=title, defaults={"description": desc, "order": i})

        # Assets ("Your Workflows Are an Asset You Keep")
        assets, _ = Section.objects.get_or_create(
            page=home, section_type="assets",
            defaults={
                "name": "Your Workflows Are an Asset",
                "heading": "Own What You Build",
                "subheading": "Every agent we build becomes part of your company's IP.",
                "order": 7,
            }
        )
        asset_points = [
            ("You Own the Data", "All workflow data and run history stays in your systems."),
            ("You Own the Models", "Fine-tuned models trained on your workflows are yours to keep."),
            ("No Vendor Lock-In", "Agents run on infrastructure you control."),
        ]
        for i, (title, desc) in enumerate(asset_points, start=1):
            SectionItem.objects.get_or_create(section=assets, title=title, defaults={"description": desc, "order": i})

        # How We Work
        how, _ = Section.objects.get_or_create(
            page=home, section_type="how_we_work",
            defaults={"name": "Our Process", "heading": "How We Work", "order": 8}
        )
        steps = [
            ("Discovery", "We map your current workflow and identify automation opportunities."),
            ("Pilot", "We build a working agent for one high-value workflow."),
            ("Deploy", "The agent goes live in your production environment."),
            ("Scale & Support", "We expand to additional workflows with ongoing support."),
        ]
        for i, (title, desc) in enumerate(steps, start=1):
            SectionItem.objects.get_or_create(section=how, title=title, defaults={"description": desc, "order": i})

        # Why Us
        why_us, _ = Section.objects.get_or_create(
            page=home, section_type="why_us",
            defaults={"name": "Why Divergent Physics", "heading": "Why Choose Us", "order": 9}
        )
        why_points = [
            ("Built by EM Experts", "Our team holds PhDs in electromagnetics and applied math."),
            ("Trusted in Production", "Deployed with a Fortune 100 client since 2025."),
            ("Backgrounds That Matter", "Team experience spans Apple and Ansys."),
        ]
        for i, (title, desc) in enumerate(why_points, start=1):
            SectionItem.objects.get_or_create(section=why_us, title=title, defaults={"description": desc, "order": i})

        # FAQ
        faq, _ = Section.objects.get_or_create(
            page=home, section_type="faq",
            defaults={"name": "Frequently Asked Questions", "heading": "FAQ", "order": 10}
        )
        faqs = [
            ("Do you support air-gapped deployments?", "Yes, our agents can run fully offline within your secured network."),
            ("Who owns the workflow IP?", "You retain full ownership of all workflow data and trained models."),
            ("How is billing structured?", "We bill on a milestone basis tied to pilot and deployment phases."),
        ]
        for i, (title, desc) in enumerate(faqs, start=1):
            SectionItem.objects.get_or_create(section=faq, title=title, defaults={"description": desc, "order": i})

        # CTA
        Section.objects.get_or_create(
            page=home, section_type="cta",
            defaults={
                "name": "Bottom CTA",
                "heading": "Bring us the workflow your engineers hate repeating",
                "button_text": "Book a Consultation",
                "button_link": "/contact",
                "order": 11,
            }
        )

        # Demo + Pricing
        demo, _ = Section.objects.get_or_create(
            page=home, section_type="demo",
            defaults={"name": "Demonstration & Pricing", "heading": "See It In Action", "order": 12}
        )
        plans = [
            ("Pilot", "Custom", "One workflow, proof of concept", ["1 workflow", "2-week delivery", "Email support"], False, 1),
            ("Growth", "Custom", "Multiple workflows, production-ready", ["Up to 5 workflows", "Priority support", "Dedicated engineer"], True, 2),
            ("Enterprise", "Contact Us", "Full-scale deployment across teams", ["Unlimited workflows", "Air-gapped option", "SLA support"], False, 3),
        ]
        for name, price, desc, features, featured, order in plans:
            PricingPlan.objects.get_or_create(
                section=demo, name=name,
                defaults={"price": price, "description": desc, "features": features,
                          "button_text": "Get Started", "button_link": "/contact",
                          "is_featured": featured, "order": order}
            )

        # Company Logos
        logos, _ = Section.objects.get_or_create(
            page=home, section_type="logos",
            defaults={"name": "Trusted By", "heading": "Companies We've Worked With", "order": 13}
        )
        logo_names = ["Apple", "Ansys", "Fortune 100 Client"]
        for i, name in enumerate(logo_names, start=1):
            SectionItem.objects.get_or_create(section=logos, title=name, defaults={"order": i})

        self.stdout.write(self.style.SUCCESS('Home page fully seeded'))

        # ================= ABOUT PAGE =================
        about_page, _ = Page.objects.get_or_create(
            name="about",
            defaults={"title": "About Us", "meta_description": "Meet the Divergent Physics team", "order": 2}
        )
        about_intro, _ = Section.objects.get_or_create(
            page=about_page, section_type="about",
            defaults={
                "name": "Team Intro",
                "heading": "Built by Engineers, for Engineers",
                "subheading": "Our team combines electromagnetics expertise with production AI engineering.",
                "order": 1,
            }
        )
        team_members = [
            ("Ali Raza", "Founder & CEO", "PhD in Electromagnetics, previously at Ansys."),
            ("Sara Khan", "Head of Engineering", "Applied math background, ex-Apple RF team."),
            ("Bilal Ahmed", "Lead AI Engineer", "Specializes in agentic workflow automation."),
        ]
        for i, (name, role, desc) in enumerate(team_members, start=1):
            SectionItem.objects.get_or_create(
                section=about_intro, name=name, role=role,
                defaults={"description": desc, "order": i}
            )
        self.stdout.write(self.style.SUCCESS('About page seeded'))

        # ================= WIRELESS PAGE =================
        wireless_page, _ = Page.objects.get_or_create(
            name="wireless",
            defaults={"title": "Wireless Systems", "meta_description": "AI agents for wireless system workflows", "order": 3}
        )

        wireless_hero, _ = Section.objects.get_or_create(
            page=wireless_page, section_type="hero",
            defaults={
                "name": "Wireless Hero",
                "heading": "AI Agents for Wireless System Design",
                "subheading": "Automate antenna array, RF front-end, and link-budget workflows.",
                "button_text": "Talk to Us",
                "button_link": "/contact",
                "order": 1,
            }
        )

        wireless_overview, _ = Section.objects.get_or_create(
            page=wireless_page, section_type="custom",
            defaults={
                "name": "Wireless Overview",
                "heading": "Where We Fit in Your Wireless Stack",
                "subheading": "From component-level EM simulation to full system link budgets.",
                "order": 2,
            }
        )
        wireless_cards = [
            ("Antenna Array Design", "Automated pattern synthesis and optimization across array configurations."),
            ("RF Front-End Simulation", "Agent-driven S-parameter sweeps and matching network tuning."),
            ("Link Budget Analysis", "End-to-end system-level performance modeling."),
        ]
        for i, (title, desc) in enumerate(wireless_cards, start=1):
            SectionItem.objects.get_or_create(section=wireless_overview, title=title, defaults={"description": desc, "order": i})

        self.stdout.write(self.style.SUCCESS('Wireless page seeded'))

        # ================= BLOG POSTS =================
        posts = [
            ("How AI Agents Are Changing RF Simulation", "A look at where manual EM workflows are headed."),
            ("Inside Our Antenna-in-Package Case Study", "A breakdown of our first production deployment."),
            ("Why Workflow Ownership Matters", "The case for keeping your simulation IP in-house."),
        ]
        for i, (title, desc) in enumerate(posts, start=1):
            BlogPost.objects.get_or_create(
                title=title,
                defaults={"description": desc, "content": desc, "order": i}
            )
        self.stdout.write(self.style.SUCCESS('Blog posts seeded'))

        self.stdout.write(self.style.SUCCESS('ALL DATA SEEDED SUCCESSFULLY'))
# ================= PLATFORM PAGE =================
        platform_page, _ = Page.objects.get_or_create(
            name="platform",
            defaults={"title": "Platform", "meta_description": "The self-serve platform behind our agents", "order": 4}
        )
        platform_hero, _ = Section.objects.get_or_create(
            page=platform_page, section_type="hero",
            defaults={
                "name": "Platform Hero",
                "heading": "Built on Our Own Platform",
                "subheading": "The same infrastructure that powers our custom agents is available self-serve.",
                "button_text": "Start Free Trial",
                "button_link": "/app/signup",
                "order": 1,
            }
        )
        platform_features, _ = Section.objects.get_or_create(
            page=platform_page, section_type="custom",
            defaults={"name": "Platform Features", "heading": "What You Get", "order": 2}
        )
        feature_items = [
            ("Agent Builder", "Visually compose multi-step simulation workflows."),
            ("Run History & Audit Trail", "Every run logged and traceable."),
            ("Solver Integrations", "Native support for Ansys HFSS and other EM solvers."),
        ]
        for i, (title, desc) in enumerate(feature_items, start=1):
            SectionItem.objects.get_or_create(section=platform_features, title=title, defaults={"description": desc, "order": i})
        self.stdout.write(self.style.SUCCESS('Platform page seeded'))