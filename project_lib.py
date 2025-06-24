"""Provides utility functions for the project."""

SINGLE_TAB_LEVEL = 4


def compare_dicts_case_insensitive(d1, d2):
    """
    Compares two dictionaries for equality, ignoring case differences.

    Args:
        d1: The first dictionary to compare.
        d2: The second dictionary to compare.

    Returns:
        bool: True if the dictionaries are equal, False otherwise.
    """
    import json

    return (
        json.dumps(d1, sort_keys=True).lower() == json.dumps(d2, sort_keys=True).lower()
    )


def print_in_box(text, title="", cols=100, tab_level=0):
    """
    Prints the given text in a box with the specified title and dimensions.

    Args:
        text: The text to print in the box.
        title: The title of the box.
        cols: The width of the box.
        tab_level: The level of indentation for the box.
    """
    import textwrap

    text = str(text)

    # Make a box using extended ASCII characters
    if cols < 4 + tab_level * SINGLE_TAB_LEVEL:
        cols = 4 + tab_level * SINGLE_TAB_LEVEL

    tabs = " " * tab_level * SINGLE_TAB_LEVEL

    top = (
        tabs
        + "\u2554"
        + "\u2550" * (cols - 2 - tab_level * SINGLE_TAB_LEVEL)
        + "\u2557"
    )
    if tab_level == 0:
        print()  # Print a newline before any box at level 0

    if title:
        # replace the middle of the top with the title
        title = "[ " + title + " ]"
        top = top[: (cols - len(title)) // 2] + title + top[(cols + len(title)) // 2 :]
    print(top)

    for line in text.split("\n"):
        for wrapped_line in textwrap.wrap(
            line, cols - 4 - tab_level * SINGLE_TAB_LEVEL
        ):
            print(
                f"{tabs}\u2551 {wrapped_line:<{cols - 4 - tab_level * SINGLE_TAB_LEVEL}} \u2551"
            )

    print(
        f"{tabs}\u255a"
        + "\u2550" * (cols - 2 - tab_level * SINGLE_TAB_LEVEL)
        + "\u255d"
    )


def do_chat_completion(messages: list[dict[str, str]], **kwargs):
    """A simple wrapper around OpenAI's chat completion API.

    Args:
        messages: A list of messages to send to the chat completion API.

    Returns:
        str: The response from the chat completion API.

    Raises:
        openai.OpenAIError: If the chat completion API returns an error.

    Examples:
        >>> messages = [
        ...     {"role": "user", "content": "Hello, how are you?"},
        ...     {"role": "assistant", "content": "I'm good, thanks!"},
        ... ]
        >>> from unittest.mock import patch
        >>> with patch('openai.OpenAI') as mock_openai:
        ...     # Setup mock response
        ...     mock_client = mock_openai.return_value
        ...     mock_chat = mock_client.chat
        ...     mock_completions = mock_chat.completions
        ...     mock_create = mock_completions.create
        ...     mock_response = mock_create.return_value
        ...     mock_response.choices = [type('obj', (object,), {'message': type('msg', (object,), {'content': "I'm good, thanks!"})()})]
        ...     response = do_chat_completion(messages)
        >>> response
        "I'm good, thanks!"
    """
    import openai

    client = openai.OpenAI(
        base_url="https://openai.vocareum.com/v1",
        api_key="voc-1528689085160736365463468376c73845a55.15105883",
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, **kwargs
    )
    return response.choices[0].message.content


EVENT_CALENDAR = [
    {
        "name": "Yoga in the Park",
        "time": "2025-06-10 13:00",
        "location": "Riverfront Stage",
        "category": "Fitness",
        "description": "Join us for a refreshing outdoor yoga session with certified instructor Maria Zen. This all-levels class will focus on breathwork, stretching, and relaxation, set against the beautiful backdrop of the Riverfront. Attendees are encouraged to bring their own mats and water. Perfect for anyone seeking to improve their mental and physical well-being in a tranquil environment. Note: This event is suitable for all ages; however, some poses may require modification for beginners or those with physical limitations.",
        "price": "10",
    },
    {
        "name": "Capture the Moment: Photography Workshop",
        "time": "2025-06-10 13:00",
        "location": "Community Center",
        "category": "Photography",
        "description": "Join us for an engaging photography workshop where participants will learn the fundamentals of photography, including composition, lighting, and editing techniques. Perfect for beginners and hobbyists! Bring your own camera or smartphone and unleash your creativity. Participants will also get the chance to showcase their work in a friendly group critiquing session at the end. All ages welcome!",
        "price": "25",
    },
    {
        "name": "AgentsVille Book Fair",
        "time": "2025-06-10 13:00",
        "location": "Community Center",
        "category": "Literature",
        "description": "Join us for the annual AgentsVille Book Fair! Discover new authors, participate in engaging workshops, and attend readings from local literary talents. A wonderful event for all ages to encourage reading and creativity.",
        "price": "10",
    },
    {
        "name": "AgentsVille Artisan Market",
        "time": "2025-06-10 13:00",
        "location": "Old Town Square",
        "category": "Crafts",
        "description": "Join us for the AgentsVille Artisan Market, a vibrant gathering of local craftspeople showcasing handmade goods. Explore unique jewelry, pottery, textiles, and artwork while supporting our community. Enjoy live music, crafting demonstrations, and a fun atmosphere for all ages!",
        "price": "20",
    },
    {
        "name": "AgentsVille Summer Jam",
        "time": "2025-06-10 15:00",
        "location": "Sports Arena",
        "category": "Music",
        "description": "Join us for the annual AgentsVille Summer Jam featuring live performances from local bands and artists! Enjoy great music, dancing, and a lively atmosphere. Bring your family and friends for an afternoon of fun and entertainment!",
        "price": "Free",
    },
    {
        "name": "Crafting for a Cause",
        "time": "2025-06-10 18:00",
        "location": "Convention Center",
        "category": "Crafts",
        "description": "Join us for an evening of creativity and community at the Crafting for a Cause event! Attendees will have the opportunity to create their own personalized crafts, with supplies provided. This event is suitable for all ages and skill levels. All materials are environmentally friendly and suitable for vegans. A portion of the proceeds will go to local charities supporting children's programs in AgentsVille.",
        "price": "5",
    },
    {
        "name": "Cinematic Under the Stars",
        "time": "2025-06-10 18:00",
        "location": "Grand Theater",
        "category": "Film",
        "description": "Join us for an enchanting evening of classic films under the stars at the Grand Theater! Bring your friends and family for a cozy outdoor screening featuring timeless favorites. Snacks and refreshments will be available for purchase. Proceeds from donations will support local arts initiatives.",
        "price": "Donation-based",
    },
    {
        "name": "Under the Stars: Poetry Night",
        "time": "2025-06-10 20:00",
        "location": "Downtown Plaza",
        "category": "Literature",
        "description": "Join us for an enchanting evening of poetry reading under the stars! Local poets will take the stage to share their works, encouraging community engagement and appreciation for the art of spoken word. Bring a blanket to sit on and enjoy the ambiance of Downtown Plaza. Ideal for poetry lovers and newcomers alike!",
        "price": "Free",
    },
    {
        "name": "Laughs Under the Stars",
        "time": "2025-06-10 20:00",
        "location": "Old Town Square",
        "category": "Comedy",
        "description": "Join us for an evening of laughter under the stars with top-notch comedians from across the country. Set in the charming Old Town Square, this comedy event promises to be a night full of joy and fun. Bring your friends and prepare for a bellyful of laughter!",
        "price": "25",
    },
    {
        "name": "Night Under the Stars: Photography Workshop",
        "time": "2025-06-10 20:00",
        "location": "Community Center",
        "category": "Photography",
        "description": "Join us for an enchanting evening of photography as we capture the beauty of the night sky. Participants will learn about astrophotography techniques and have the opportunity to try them out with provided telescopes and cameras. Bring your own camera if you have one! This workshop is suitable for all skill levels, and a portion of the donations will go to local art initiatives. No prior experience necessary.",
        "price": "Donation-based",
    },
    {
        "name": "Laughter Fest 2025",
        "time": "2025-06-11 10:00",
        "location": "Cultural Center",
        "category": "Comedy",
        "description": "Join us for a morning of laughter at the Laughter Fest 2025! Enjoy stand-up performances from top comedians, along with surprise guests that will leave you in stitches. This event is perfect for those aged 18 and up, and it promises to be a fun-filled experience for everyone!",
        "price": "50",
    },
    {
        "name": "Summer Serenades",
        "time": "2025-06-11 10:00",
        "location": "Botanical Gardens",
        "category": "Music",
        "description": "Join us at the beautiful Botanical Gardens for a captivating morning of live music performances. Enjoy an array of local bands playing a mix of genres while surrounded by breathtaking floral displays. Bring a picnic blanket and relax in the sun with family and friends!",
        "price": "25",
    },
    {
        "name": "AgentsVille Summer Festival",
        "time": "2025-06-11 13:00",
        "location": "Old Town Square",
        "category": "Festival",
        "description": "Join us for the annual AgentsVille Summer Festival, a day filled with live music, dance performances, and local artisans showcasing their crafts. Enjoy delicious food from various food trucks featuring selections including vegan tacos, gluten-free pizza, and scrumptious desserts. Plenty of activities for kids, and there's a special petting zoo for the little ones!",
        "price": "40",
    },
    {
        "name": "AgentsVille Summer Music Fest",
        "time": "2025-06-11 13:00",
        "location": "Convention Center",
        "category": "Music",
        "description": "Join us for the AgentsVille Summer Music Fest featuring live performances from local bands, food trucks, and a vibrant arts & crafts market. Enjoy a variety of music genres, family-friendly activities, and the chance to support local talent!",
        "price": "50",
    },
    {
        "name": "Afternoon Acoustic Session",
        "time": "2025-06-11 15:00",
        "location": "Public Library",
        "category": "Music",
        "description": "Join us for a cozy afternoon of live acoustic music featuring local artists. Enjoy soothing melodies while surrounded by the serene atmosphere of the library. This event is perfect for music lovers of all ages. Bring a friend or family member and relax!",
        "price": "Donation-based",
    },
    {
        "name": "AgentsVille Summer Festival",
        "time": "2025-06-11 18:00",
        "location": "Downtown Plaza",
        "category": "Family",
        "description": "Join us for the annual AgentsVille Summer Festival! This family-friendly event features fun games, live music, and a variety of activities for all ages. Enjoy delicious food like grilled corn on the cob, cheeseburgers, vegan tacos, and gluten-free brownie bites. Don't miss out on the exciting face painting for kids and the evening's spectacular firework display!",
        "price": "40",
    },
    {
        "name": "AgentsVille Historical Walk",
        "time": "2025-06-11 18:00",
        "location": "Cultural Center",
        "category": "History",
        "description": "Join us for an enlightening evening as we explore the rich history of AgentsVille on our guided historical walk. The event will feature expert local historians who will share fascinating stories and insights about the town's past, leading participants through significant historical sites. Get ready to learn, engage, and marvel at the legacy of our vibrant town!",
        "price": "40",
    },
    {
        "name": "AgentsVille Cooking Class: Italian Night",
        "time": "2025-06-11 19:30",
        "location": "Public Library",
        "category": "Culinary",
        "description": "Join us for a delightful evening of Italian cooking! We'll be making classic dishes such as homemade pasta, marinara sauce, and tiramisu, all from scratch. This hands-on class is perfect for all skill levels. Participants will enjoy tasting each dish. Please note, all dishes are vegetarian, and we can accommodate gluten-free substitutes if requested in advance. Come hungry and ready to learn!",
        "price": "Donation-based",
    },
    {
        "name": "Poetry Under the Stars",
        "time": "2025-06-11 20:00",
        "location": "Botanical Gardens",
        "category": "Literature",
        "description": "Join us for a magical evening of poetry readings under the stars, featuring local poets and immersive performances. Bring a blanket to sit on and enjoy the beauty of nature while you listen to heartfelt verses. Perfect for poetry lovers of all ages!",
        "price": "30",
    },
    {
        "name": "Midsummer Night's Dream",
        "time": "2025-06-11 20:00",
        "location": "University Campus",
        "category": "Theater",
        "description": "Join us for a magical evening as the University Theater presents Shakespeare's enchanting comedy, 'Midsummer Night's Dream.' Experience a captivating performance filled with love, mischief, and fairies under the moonlit sky.",
        "price": "30",
    },
    {
        "name": "Whispers of the Wind Poetry Festival",
        "time": "2025-06-12 10:00",
        "location": "Old Town Square",
        "category": "Poetry",
        "description": "Join us for the Whispers of the Wind Poetry Festival in the heart of AgentsVille! Experience an inspiring day with local poets sharing their works and engaging in open mic sessions. Enjoy a creative atmosphere, live music, and the opportunity to connect with fellow poetry enthusiasts. Don't miss our special guest poet who will be delivering a keynote address. Suitable for all ages.",
        "price": "30",
    },
    {
        "name": "Taste of AgentsVille",
        "time": "2025-06-12 10:00",
        "location": "City Museum",
        "category": "Food",
        "description": "Join us for the annual Taste of AgentsVille, where local chefs showcase their best dishes! Enjoy a variety of delectable offerings including gluten-free pasta, vegan curry, and traditional peach cobbler. Come hungry and sample tasty bites from all around town!",
        "price": "Free",
    },
    {
        "name": "Yoga in the Gallery",
        "time": "2025-06-12 13:00",
        "location": "Art Gallery",
        "category": "Fitness",
        "description": "Join us for a refreshing yoga session amidst beautiful artworks at the Art Gallery. This class is suitable for all levels and will be led by certified instructors. Bring your own mat and water bottle. Perfect for stress relief and flexibility!",
        "price": "10",
    },
    {
        "name": "Annual Fitness Expo",
        "time": "2025-06-12 15:00",
        "location": "Convention Center",
        "category": "Fitness",
        "description": "Join us for the Annual Fitness Expo where you can participate in various workshops, fitness demonstrations, and meet fitness experts. Discover new workout routines, healthy living tips, and exciting fitness gear. All levels of fitness enthusiasts are welcome!",
        "price": "30",
    },
    {
        "name": "Science Odyssey: A Day of Discovery",
        "time": "2025-06-12 15:00",
        "location": "City Museum",
        "category": "Science",
        "description": "Join us for an interactive exploration of the wonders of science! This event features engaging demonstrations, hands-on experiments, and lectures from renowned scientists. Suitable for all ages, attendees will learn about physics, chemistry, and biology through fun and exciting activities. Don't miss out on the chance to spark curiosity and imagination!",
        "price": "50",
    },
    {
        "name": "AgentsVille Tech Expo 2025",
        "time": "2025-06-12 18:00",
        "location": "Downtown Plaza",
        "category": "Technology",
        "description": "Join us for the AgentsVille Tech Expo 2025, a showcase of innovative technologies and tech start-ups in our town! Network with industry experts and get hands-on experience with the latest gadgets. Enjoy interactive workshops, keynote speakers, and an exhibition area featuring cutting-edge products. Don't miss the opportunity to learn about the future of technology!",
        "price": "25",
    },
    {
        "name": "Understanding Artificial Intelligence",
        "time": "2025-06-12 19:30",
        "location": "Public Library",
        "category": "Education",
        "description": "Join us for an enlightening workshop on the basics of Artificial Intelligence. Learn how AI is transforming our world through practical examples and interactive discussions. Open to all ages, this event will feature local experts who will simplify complex topics and answer your burning questions.",
        "price": "Donation-based",
    },
    {
        "name": "Evening of Quantum Curiosities",
        "time": "2025-06-12 19:30",
        "location": "Public Library",
        "category": "Science",
        "description": "Join us for an enlightening evening delving into the mysteries of quantum physics. Renowned physicist Dr. Ellen Quark will lead a captivating talk and Q&A session on the principles of quantum mechanics, making complex topics accessible to all. Whether you're a science enthusiast or simply curious, this event promises to be both educational and engaging!",
        "price": "10",
    },
    {
        "name": "Starlit Poetry Night",
        "time": "2025-06-12 20:00",
        "location": "City Museum",
        "category": "Poetry",
        "description": "Join us for a magical evening of poetry under the stars in the beautiful gardens of the City Museum. Local poets will share their work, and audience members are encouraged to participate in an open mic segment. The event will also feature ambient music and a cozy atmosphere perfect for inspiration.",
        "price": "Free",
    },
    {
        "name": "Stargazing Night: The Wonders of the Universe",
        "time": "2025-06-12 20:00",
        "location": "Community Center",
        "category": "Science",
        "description": "Join us for a mesmerizing evening of stargazing and astronomy! Experts will guide you through the night sky, highlighting constellations, planets, and galaxies visible to the naked eye. Telescopes will be provided for those who want a closer look. Bring your blanket and enjoy this cosmic adventure! Perfect for families and space enthusiasts. The event is rain or shine, with indoor activities planned in case of inclement weather.",
        "price": "15",
    },
    {
        "name": "Sunny Shores Festival",
        "time": "2025-06-13 10:00",
        "location": "Beach Boardwalk",
        "category": "Festival",
        "description": "Join us for the annual Sunny Shores Festival at the scenic Beach Boardwalk! Enjoy live music, artisan craft booths, and activities for all ages. Savor delicious local food offerings including fresh seafood tacos, vegan burgers, and gluten-free desserts, all while enjoying the beautiful ocean view. Don’t miss this lively celebration of community and summer fun!",
        "price": "5",
    },
    {
        "name": "AgentsVille Family Fun Day",
        "time": "2025-06-13 13:00",
        "location": "Sports Arena",
        "category": "Family",
        "description": "Join us for a day filled with games, activities, and entertainment for the whole family! Enjoy face painting, a bouncy castle, and live performances. There will be fun contests with great prizes, and a chance to meet local mascots!",
        "price": "25",
    },
    {
        "name": "AgentsVille Summer Splash Festival",
        "time": "2025-06-13 13:00",
        "location": "Beach Boardwalk",
        "category": "Festival",
        "description": "Join us for the annual AgentsVille Summer Splash Festival! Enjoy live music, exciting games, and various water activities suitable for families. Indulge in delicious summer treats, including grilled corn on the cob, watermelon slices, and a variety of ice cream flavors (including dairy-free options). Bring your sunscreen and enjoy a day of fun and relaxation by the beach!",
        "price": "10",
    },
    {
        "name": "AgentsVille Community Cook-off",
        "time": "2025-06-13 13:00",
        "location": "Historic District",
        "category": "Culinary",
        "description": "Join us for the annual AgentsVille Community Cook-off, where local chefs and home cooks will showcase their culinary skills! Enjoy a variety of dishes including vegetarian pasta salad, spicy vegan chili, and succulent barbecue pulled pork, perfect for all tastes. Gluten-free and nut-free options will also be available. Taste the flavors of our town while supporting local culinary talent!",
        "price": "Donation-based",
    },
    {
        "name": "AgentsVille Food Festival",
        "time": "2025-06-13 15:00",
        "location": "Historic District",
        "category": "Culinary",
        "description": "Join us for the AgentsVille Food Festival, where local chefs showcase their best dishes! Enjoy a variety of mouth-watering options including vegan tacos, gluten-free pasta, and a chocolate fountain. There will be something for everyone, including options for those with dietary restrictions such as nut-free and lactose-free dishes. Bring your appetite and enjoy a day full of flavor!",
        "price": "20",
    },
    {
        "name": "Culinary Delights: Tasting Evening",
        "time": "2025-06-13 18:00",
        "location": "Public Library",
        "category": "Food",
        "description": "Join us for a delightful evening of culinary tasting featuring a variety of international dishes. Enjoy vegan and gluten-free options alongside flavorful meat and dairy platters. Sample dishes from around the world and learn about the cultural significance behind each cuisine.",
        "price": "15",
    },
    {
        "name": "Taste of AgentsVille",
        "time": "2025-06-13 19:30",
        "location": "Historic District",
        "category": "Food",
        "description": "Join us for the annual Taste of AgentsVille, where local chefs showcase their culinary talents. Enjoy a variety of dishes, including vegan and gluten-free options. Featuring signature dishes like homemade pasta, barbecue pulled jackfruit sliders, and artisanal desserts to satisfy your sweet tooth. Perfect for food lovers of all dietary preferences!",
        "price": "5",
    },
    {
        "name": "Outdoor Yoga Under the Stars",
        "time": "2025-06-13 19:30",
        "location": "University Campus",
        "category": "Fitness",
        "description": "Join us for an evening of relaxation and rejuvenation with our Outdoor Yoga Under the Stars event! Experience the serenity of yoga while surrounded by nature. All levels are welcome, and please bring your own yoga mat. Enjoy a light refreshing herbal tea post-session, ideal for all dietary preferences including gluten-free and vegan options!",
        "price": "10",
    },
    {
        "name": "AgentsVille Annual Photography Exhibition",
        "time": "2025-06-13 19:30",
        "location": "Art Gallery",
        "category": "Photography",
        "description": "Join us for the AgentsVille Annual Photography Exhibition featuring local and international photographers showcasing their best works. Enjoy a night of creativity and inspiration as you explore various photography styles, including landscape, portrait, and abstract. A limited number of prints will be available for purchase. Refreshments will be provided, including gourmet finger foods, vegan snacks, and gluten-free options. Don't miss this opportunity to celebrate artistry in our vibrant community!",
        "price": "50",
    },
    {
        "name": "AgentsVille Arts Festival",
        "time": "2025-06-13 20:00",
        "location": "Sports Arena",
        "category": "Arts",
        "description": "Join us for the AgentsVille Arts Festival, a night celebrating local artists and their creative works! Enjoy live performances, art exhibits, and interactive art stations. Bring your loved ones and immerse yourself in the vibrant culture of AgentsVille! Admission is donation-based, with all proceeds going towards community arts programs.",
        "price": "Donation-based",
    },
    {
        "name": "Sunrise Photography Workshop",
        "time": "2025-06-14 10:00",
        "location": "University Campus",
        "category": "Photography",
        "description": "Join us for a captivating workshop where you'll learn the art of capturing stunning sunrise photos. Led by local photography expert Mia Rivers, this workshop is suitable for all skill levels. Make sure to bring your camera and tripod!",
        "price": "30",
    },
    {
        "name": "Laughter in the Park",
        "time": "2025-06-14 10:00",
        "location": "Historic District",
        "category": "Comedy",
        "description": "Join us for a morning of laughter at the Historic District of AgentsVille! 'Laughter in the Park' features a lineup of local comedians who will have you rolling in the aisles with their hilarious takes on everyday life. Bring your friends and family for a fun-filled outdoor comedy experience under the sun!",
        "price": "30",
    },
    {
        "name": "Starry Night Science Spectacular",
        "time": "2025-06-14 18:00",
        "location": "Riverfront Stage",
        "category": "Science",
        "description": "Join us for an evening of fascinating astronomical discoveries and hands-on activities as we explore the wonders of the universe. Engage with local scientists and enjoy stargazing through telescopes after the presentations. Perfect for families and those curious about the cosmos!",
        "price": "10",
    },
    {
        "name": "Laughter Under the Stars",
        "time": "2025-06-14 19:30",
        "location": "Cultural Center",
        "category": "Comedy",
        "description": "Join us for a night of laughter featuring local comedians as they take the stage to share their wittiest jokes and stories. It's a perfect evening for friends and family!",
        "price": "Free",
    },
    {
        "name": "Sonnets Under the Stars",
        "time": "2025-06-14 19:30",
        "location": "Cultural Center",
        "category": "Poetry",
        "description": "Join us for an enchanting evening of poetry where local poets will share their sonnets and spoken word pieces under the stars. The event aims to celebrate the power of words and the beauty of expression with a cozy and intimate atmosphere.",
        "price": "15",
    },
    {
        "name": "Gourmet Food Fest",
        "time": "2025-06-14 19:30",
        "location": "Sports Arena",
        "category": "Food",
        "description": "Join us for an evening of culinary delights at the Gourmet Food Fest! Enjoy a diverse selection of dishes from local chefs, featuring gluten-free, vegetarian, and vegan options. Indulge in mouth-watering appetizers, savory entrees, and delectable desserts while mingling with fellow food enthusiasts. Experience the flavors of AgentsVille like never before!",
        "price": "50",
    },
    {
        "name": "AgentsVille Family Movie Night",
        "time": "2025-06-14 19:30",
        "location": "Grand Theater",
        "category": "Family",
        "description": "Join us for an enchanting evening of family-friendly films! Enjoy a double feature showcasing classic animated movies that are sure to delight audiences of all ages. Come early to grab your favorite seat and participate in fun games and activities before the show!",
        "price": "Donation-based",
    },
    {
        "name": "AgentsVille Craft Fair",
        "time": "2025-06-14 20:00",
        "location": "Historic District",
        "category": "Crafts",
        "description": "Join us in the Historic District for the annual AgentsVille Craft Fair! Explore a variety of handmade crafts from local artisans, including pottery, jewelry, textiles, and woodwork. A great opportunity to pick up unique gifts and support local artists. Suitable for all ages!",
        "price": "20",
    },
    {
        "name": "AgentsVille Summer Food Festival",
        "time": "2025-06-14 20:00",
        "location": "Sports Arena",
        "category": "Culinary",
        "description": "Join us for a delightful evening at the AgentsVille Summer Food Festival! Savor an array of gourmet food from local vendors, featuring grilled shrimp tacos, vegan stir-fried noodles, and decadent chocolate mousse. All food options will be clearly labeled for allergens, with vegetarian and gluten-free selections available. Bring your appetite and enjoy live music while you taste the best our town has to offer!",
        "price": "30",
    },
    {
        "name": "Future Tech Showcase",
        "time": "2025-06-14 20:00",
        "location": "City Museum",
        "category": "Technology",
        "description": "Join us for an evening of innovation at the Future Tech Showcase, where cutting-edge technology meets creativity. Explore interactive exhibits showcasing the latest advancements in AI, robotics, virtual reality, and more. Meet industry leaders and visionary inventors who are shaping our tech-filled future. Don't miss this chance to network with fellow tech enthusiasts!",
        "price": "40",
    },
    {
        "name": "Summer Spectacular: A Musical Journey",
        "time": "2025-06-15 10:00",
        "location": "Community Center",
        "category": "Theater",
        "description": "Join us for the Summer Spectacular, an engaging musical theater performance featuring local talents. This event showcases a series of original songs and classic hits, suitable for all ages. Enjoy a lively atmosphere and witness the magic of theater come to life!",
        "price": "15",
    },
    {
        "name": "AgentsVille Science Fair",
        "time": "2025-06-15 10:00",
        "location": "Riverfront Stage",
        "category": "Education",
        "description": "Join us for the annual AgentsVille Science Fair where local students showcase their innovative science projects! Expect hands-on experiments, fascinating demonstrations, and the chance to vote for your favorite project. Ideal for families and science enthusiasts alike!",
        "price": "25",
    },
    {
        "name": "AgentsVille Arts Festival",
        "time": "2025-06-15 10:00",
        "location": "Old Town Square",
        "category": "Arts",
        "description": "Join us for the annual AgentsVille Arts Festival, showcasing local artists and crafters. Explore unique artworks, photography, and handmade crafts while enjoying live music and entertainment. Perfect for art lovers of all ages!",
        "price": "15",
    },
    {
        "name": "AgentsVille Artisan Market",
        "time": "2025-06-15 13:00",
        "location": "Botanical Gardens",
        "category": "Market",
        "description": "Join us for the AgentsVille Artisan Market at the stunning Botanical Gardens! Browse unique handmade crafts, local art, and delicious gourmet food from various vendors. Enjoy live music while you explore the offerings. Vegan, gluten-free, and nut-free options will be available to cater to all dietary needs.",
        "price": "30",
    },
    {
        "name": "AgentsVille Summer Craft Fair",
        "time": "2025-06-15 13:00",
        "location": "Central Park",
        "category": "Crafts",
        "description": "Join us in Central Park for the AgentsVille Summer Craft Fair! Enjoy a delightful afternoon immersed in creativity with local artisans showcasing their handmade goods. Participate in interactive craft workshops suitable for all ages, and create your own unique art pieces to take home. Ideal for families, friends, and anyone looking to unleash their inner artist!",
        "price": "5",
    },
    {
        "name": "AgentsVille Family Fun Day",
        "time": "2025-06-15 13:00",
        "location": "Downtown Plaza",
        "category": "Family",
        "description": "Join us for a day of fun activities for the whole family! Enjoy games, face painting, live music, and a variety of food stalls featuring delicious options including vegan and gluten-free treats. There will also be a bouncy castle and a petting zoo for kids of all ages!",
        "price": "20",
    },
    {
        "name": "History of the Botanical Gardens Tour",
        "time": "2025-06-15 13:00",
        "location": "Botanical Gardens",
        "category": "History",
        "description": "Join us for an enlightening tour through the rich history of the Botanical Gardens. Discover the rare plant collections, learn about the garden's development over the years, and enjoy beautiful landscapes while guided by a knowledgeable historian. Perfect for history buffs and nature lovers alike!",
        "price": "15",
    },
    {
        "name": "Discover the Stars: An Astronomy Exhibition",
        "time": "2025-06-15 15:00",
        "location": "Art Gallery",
        "category": "Science",
        "description": "Join us for an enlightening afternoon at the Art Gallery as we explore the wonders of astronomy. This exhibition features stunning visuals of celestial phenomena, interactive displays, and guest speakers from the local astronomy club who will share their insights about the universe. Perfect for all ages!",
        "price": "25",
    },
    {
        "name": "Shakespeare Under the Stars",
        "time": "2025-06-15 18:00",
        "location": "Public Library",
        "category": "Theater",
        "description": "Join us for a magical evening of theater featuring a performance of Shakespeare's timeless classic, 'A Midsummer Night's Dream.' Experience the enchanting world of fairies and romance right in your local park. Seating is available on a first-come, first-served basis, so arrive early to secure a good spot.",
        "price": "40",
    },
    {
        "name": "Artisan Craft Night",
        "time": "2025-06-15 19:30",
        "location": "Art Gallery",
        "category": "Crafts",
        "description": "Join us for an enchanting evening at the Art Gallery for Artisan Craft Night. Attendees will have the opportunity to create beautiful handmade crafts with guidance from talented local artists. All materials will be provided, and no prior experience is necessary. Perfect for all skill levels!",
        "price": "50",
    },
]

WEATHER_FORECAST = [
    {
        "date": "2025-06-10",
        "city": "AgentsVille",
        "temperature": 31,
        "temperature_unit": "celsius",
        "condition": "clear",
        "description": "A bright and sunny day in AgentsVille with clear skies and warm temperatures. Perfect weather for outdoor activities!",
    },
    {
        "date": "2025-06-11",
        "city": "AgentsVille",
        "temperature": 34,
        "temperature_unit": "celsius",
        "condition": "partly cloudy",
        "description": "A warm day with periods of sunshine and mixed clouds, making it a perfect opportunity for outdoor activities.",
    },
    {
        "date": "2025-06-12",
        "city": "AgentsVille",
        "temperature": 28,
        "temperature_unit": "celsius",
        "condition": "thunderstorm",
        "description": "A thunderstorm is expected to roll in during the afternoon, bringing heavy rain and gusty winds. The atmosphere will feel charged with humidity, creating a sultry and dramatic setting as clouds build in the sky.",
    },
    {
        "date": "2025-06-13",
        "city": "AgentsVille",
        "temperature": 15,
        "temperature_unit": "celsius",
        "condition": "rainy",
        "description": "Cloudy skies with intermittent rain showers throughout the day, accompanied by a cool breeze and a chance of occasional thunderstorms.",
    },
    {
        "date": "2025-06-14",
        "city": "AgentsVille",
        "temperature": 14,
        "temperature_unit": "celsius",
        "condition": "rainy",
        "description": "A steady rain is expected throughout the day with overcast skies and cool temperatures. Residents should be prepared for slick roads and carry umbrellas.",
    },
    {
        "date": "2025-06-15",
        "city": "AgentsVille",
        "temperature": 31,
        "temperature_unit": "celsius",
        "condition": "sunny",
        "description": "A bright and sunny day perfect for outdoor activities with no chance of rain.",
    },
]


def get_events(date: str, city: str, max_events=5) -> list[dict[str, str | int]]:
    """Returns a list of events for a given date and city.

    Args:
        date: The date to get events for. Must be in the format YYYY-MM-DD.
        city: The city to get events for.

    Returns:
        A list of events for the given date and city. Currently only returns events
        for AgentsVille between 2025-06-10 and 2025-06-15.

    Examples:
        >>> from pprint import pprint
        >>> pprint(get_events("2025-06-10", "AgentsVille")[0])
        {'category': 'Fitness',
         'description': 'Join us for a refreshing outdoor yoga session with certified '
                        'instructor Maria Zen. This all-levels class will focus on '
                        'breathwork, stretching, and relaxation, set against the '
                        'beautiful backdrop of the Riverfront. Attendees are '
                        'encouraged to bring their own mats and water. Perfect for '
                        'anyone seeking to improve their mental and physical '
                        'well-being in a tranquil environment. Note: This event is '
                        'suitable for all ages; however, some poses may require '
                        'modification for beginners or those with physical '
                        'limitations.',
         'location': 'Riverfront Stage',
         'name': 'Yoga in the Park',
         'price': '10',
         'time': '2025-06-10 13:00'}
    """
    import datetime

    # If the city is not AgentsVille, return an empty list
    if city != "AgentsVille":
        return []

    # Verify the date format
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {date}")
        return []

    # If the date is not between 2025-06-10 and 2025-06-15, return an empty list
    if date < "2025-06-10" or date > "2025-06-15":
        print(f"Date {date} is outside the valid range (2025-06-10 - 2025-06-15)")
        return []

    return [event for event in EVENT_CALENDAR if event["time"].startswith(date)][
        max_events:
    ]


def get_weather(date: str, city: str) -> dict[str, str | int]:
    """
    Returns the weather forecast for a given date and city.

    Args:
        date: The date to get weather for. Must be in the format YYYY-MM-DD.
        city: The city to get weather for.

    Returns:
        A dictionary containing the weather forecast for the given date and city.
    """
    import datetime

    # If the city is not AgentsVille, return an empty dictionary
    if city != "AgentsVille":
        return {}

    # Verify the date format
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"Invalid date format: {date}")
        return {}

    # If the date is not between 2025-06-10 and 2025-06-15, return an empty dictionary
    if date < "2025-06-10" or date > "2025-06-15":
        print(f"Date {date} is outside the valid range (2025-06-10 - 2025-06-15)")
        return {}

    return next(
        (forecast for forecast in WEATHER_FORECAST if forecast["date"] == date), {}
    )


def narrate_my_trip(vacation_info, itinerary, filename="speech.mp3"):
    from IPython.display import Audio, Markdown, display
    from openai import OpenAI

    resp = do_chat_completion(
        messages=[
            {
                "role": "user",
                "content": f"""
                Here is information on the trip collected by the Onboarding Agent:
                {vacation_info}.

                Here is the final itinerary:
                {itinerary}
                
                Introduce the trip (travelers, interests, restrictions, and total cost) and
                then discuss each day of the itinerary.

                Do not specify the cost of each activity.

                Do not reference the the narrative itself in the response.
                """,
            }
        ]
    )
    display(Markdown(resp))

    client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key="voc-1528689085160736365463468376c73845a55.15105883",
    )

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=resp,
        instructions="Speak in a cheerful and positive tone.",
    ) as response:
        response.stream_to_file(filename)

    display(Audio(filename))
