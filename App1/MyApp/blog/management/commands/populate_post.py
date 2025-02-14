from blog.models import Post,Category
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help ="This Command inserts post data"

    def handle(self, *args:any,**options:any):
        
        #Delete Existing Data
        Post.objects.all().delete()
        titles = [
            "Revolutionizing Embedded Systems with FPGA",
            "Optimizing Image Processing Using Verilog",
            "Efficient Data Processing with Parallel Prefix Adders",
            "Automation and AI: The Future of Smart Industries",
            "Enhancing Cloud Security with Python-Based Solutions",
            "Low-Power VLSI Design for Next-Gen Processors",
            "IP Verification Strategies for High-Performance Chips",
            "Advanced Computer Vision Using YOLO and Python",
            "Building Scalable Web Applications with Django",
            "Networking and Cybersecurity in the IoT Era",
            "Machine Learning in Edge Computing Devices",
            "Blockchain for Secure IoT Communication",
            "AI-Powered Predictive Maintenance in Manufacturing",
            "Big Data Analytics for Smart Cities",
            "Next-Generation Wireless Communication with 6G",
            "Robotics and Automation in Healthcare",
            "Quantum Computing and Its Impact on AI",
            "High-Speed Memory Architectures for AI Workloads",
            "Software-Defined Networking and Its Applications",
            "Neuromorphic Computing for Real-Time AI Processing",
            "Wearable Technology and Smart Healthcare",
            "Cloud-Native Architectures for Scalable AI Systems",
            "Deep Learning Acceleration with FPGA",
            "Cyber-Physical Systems in Industry 4.0",
            "Autonomous Vehicles: AI and Sensor Fusion",
            "Edge AI for Real-Time Video Analytics",
            "Human-Robot Interaction in AI-Powered Workspaces",
            "Securing AI Models Against Adversarial Attacks",
            "Optimizing Power Efficiency in AI Hardware",
            "The Role of AI in Personalized Medicine",
            "Next-Gen Storage Solutions for Big Data",
            "Green Computing and Sustainable IT Solutions",
            "AI Ethics and Responsible Machine Learning",
            "Digital Twins and Their Industrial Applications",
            "Future Trends in AI and Embedded Systems"
        ]

        contents = [
            "A breathtaking sunset over rolling hills, with golden light reflecting off a winding river, creating a stunning natural masterpiece.",
            "A city skyline illuminated at night, skyscrapers glowing as cars leave streaks of red and white light, embodying the energy of an urban metropolis.",
            "A peaceful lake mirrors towering mountains and dense forests, with mist rolling over the still waters, offering an untouched natural beauty.",
            "A winding path through a dense autumn forest, with vibrant red and orange leaves forming a natural carpet underfoot.",
            "Snow-covered peaks glistening under the bright sun, with a single traveler leaving footprints in the untouched white landscape.",
            "A golden wheat field stretching endlessly, swaying gently in the wind as birds fly overhead, singing in harmony with nature.",
            "A rustic wooden bridge over a slow-flowing river, its weathered planks adding charm to the picturesque landscape.",
            "Morning mist over a lush green valley, with the first rays of the sun casting a golden glow over dewdrop-covered grass.",
            "A coastal highway winding along the cliffs, overlooking the vast blue ocean as waves crash against the jagged rocks below.",
            "Cherry blossoms in full bloom, forming a pink tunnel along a serene pathway, filling the air with a sweet floral fragrance.",
            "A lighthouse standing tall against a stormy sky, its beam cutting through the darkness as waves crash against the rocky shore.",
            "A futuristic cityscape, filled with neon lights and flying vehicles, depicting an advanced urban setting straight out of science fiction.",
            "A tranquil garden with koi fish swimming in a crystal-clear pond, surrounded by bamboo trees and delicate water lilies.",
            "A grand ancient castle standing atop a hill, with towering stone walls and flags fluttering in the wind against a moody sky.",
            "A futuristic space station orbiting a distant planet, with astronauts floating in zero gravity against a backdrop of stars.",
            "A robot workshop filled with mechanical limbs and digital schematics, showcasing cutting-edge innovation in artificial intelligence.",
            "A bustling marketplace in a historic town, with colorful lanterns hanging overhead and vendors selling exotic goods.",
            "A deep underground cave with glowing bioluminescent fungi, illuminating the rock formations in eerie shades of blue and green.",
            "A scenic vineyard on a hillside, with rows of grapevines bathed in the golden glow of the setting sun.",
            "A cyberpunk alley lit with neon signs, casting reflections onto rain-soaked streets in a futuristic urban landscape.",
            "A majestic waterfall cascading down moss-covered rocks into a crystal-clear pool, surrounded by dense tropical rainforest.",
            "A high-tech control center, with massive screens displaying real-time data and engineers monitoring global systems.",
            "A remote desert landscape with towering sand dunes, their shifting patterns creating mesmerizing textures under the sun.",
            "An enchanted forest at twilight, with glowing fireflies dancing among the ancient, twisted trees.",
            "A glass observatory perched on a mountaintop, offering a panoramic view of the stars and distant galaxies.",
            "A futuristic self-sustaining eco-city, featuring green rooftops, solar panels, and automated energy-efficient systems.",
            "A submarine exploring the deep ocean, with glowing deep-sea creatures surrounding the vessel in an eerie, alien-like world.",
            "A modern skyscraper with transparent glass floors, offering a dizzying view of the bustling city below.",
            "A digital art installation with holographic projections, creating an immersive futuristic experience.",
            "A high-speed bullet train cutting through a snowy mountain range, blending technology and nature in perfect harmony.",
            "A floating island in the sky, with waterfalls pouring into the clouds below, forming a dreamlike fantasy landscape.",
            "A mysterious abandoned laboratory filled with overgrown vines and old computers flickering with cryptic data.",
            "A massive underground data center, its walls lined with blinking server racks processing vast amounts of information.",
            "A neon-lit gaming arena filled with players immersed in the latest VR technology, competing in a high-stakes tournament."
        ]

        img_urls = [
            "https://picsum.photos/id/101/800/400",
            "https://picsum.photos/id/102/800/400",
            "https://picsum.photos/id/103/800/400",
            "https://picsum.photos/id/104/800/400",
            "https://picsum.photos/id/96/800/400",
            "https://picsum.photos/id/106/800/400",
            "https://picsum.photos/id/107/800/400",
            "https://picsum.photos/id/108/800/400",
            "https://picsum.photos/id/109/800/400",
            "https://picsum.photos/id/110/800/400",
            "https://picsum.photos/id/111/800/400",
            "https://picsum.photos/id/112/800/400",
            "https://picsum.photos/id/113/800/400",
            "https://picsum.photos/id/114/800/400",
            "https://picsum.photos/id/115/800/400",
            "https://picsum.photos/id/116/800/400",
            "https://picsum.photos/id/117/800/400",
            "https://picsum.photos/id/118/800/400",
            "https://picsum.photos/id/119/800/400",
            "https://picsum.photos/id/120/800/400",
            "https://picsum.photos/id/121/800/400",
            "https://picsum.photos/id/122/800/400",
            "https://picsum.photos/id/123/800/400",
            "https://picsum.photos/id/124/800/400",
            "https://picsum.photos/id/125/800/400",
            "https://picsum.photos/id/126/800/400",
            "https://picsum.photos/id/127/800/400",
            "https://picsum.photos/id/128/800/400",
            "https://picsum.photos/id/129/800/400",
            "https://picsum.photos/id/130/800/400",
            "https://picsum.photos/id/131/800/400",
            "https://picsum.photos/id/132/800/400",
            "https://picsum.photos/id/133/800/400",
            "https://picsum.photos/id/134/800/400",
            "https://picsum.photos/id/135/800/400"
        ]


        categories=Category.objects.all()

        for title,content,img_url in zip(titles,contents,img_urls):
            category=random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))