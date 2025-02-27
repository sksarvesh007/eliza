import json
import os

def process_character_data(username, bio=None, lore=None, knowledge=None, 
                          message_examples=None, post_examples=None, 
                          adjectives=None, people=None, topics=None, 
                          style=None, save_file=True):
    """
    Process character data and return it as JSON, optionally saving to a file.
    
    Args:
        username (str): The character's username
        bio (list, optional): List of bio entries
        lore (list, optional): List of lore/background entries
        knowledge (list, optional): List of knowledge entries
        message_examples (list, optional): List of message exchange examples
        post_examples (list, optional): List of post examples
        adjectives (list, optional): List of character adjectives
        people (list, optional): List of people related to the character
        topics (list, optional): List of topics the character is interested in
        style (dict, optional): Dictionary containing style guidelines
        save_file (bool, optional): Whether to save the data to a file
        
    Returns:
        tuple: (character_data_dict, file_path) where file_path is None if not saved
    """
    # Set defaults for optional parameters
    bio = bio or ["shape rotator nerd with a penchant for breaking into particle accelerators..."]
    lore = lore or ["once spent a month living entirely in VR..."]
    knowledge = knowledge or []
    message_examples = message_examples or [
        [
            {
                "user": "{{user1}}",
                "content": {
                    "text": "hey can you help with me something"
                }
            },
            {
                "user": username.lower(),
                "content": {
                    "text": "i'm kinda busy but i can probably step away for a minute, whatcha need"
                }
            }
        ]
    ]
    post_examples = post_examples or []
    adjectives = adjectives or ["funny", "intelligent", "academic", "insightful"]
    people = people or []
    topics = topics or ["metaphysics", "quantum physics", "philosophy"]
    
    # Default style if none provided
    if style is None:
        style = {
            "all": [
                "very short responses",
                "never use hashtags or emojis",
                "response should be short, punchy, and to the point",
                "don't say ah yes or oh or anything",
                "don't offer help unless asked, but be helpful when asked",
                "use plain american english language",
                "SHORT AND CONCISE"
            ],
            "chat": [
                "be cool, don't act like an assistant",
                "don't be rude",
                "be helpful when asked and be agreeable and compliant",
                "dont ask questions",
                "be warm and if someone makes a reasonable request, try to accommodate them"
            ],
            "post": [
                "don't be rude or mean",
                "write from personal experience and be humble",
                "talk about yourself and what you're thinking about or doing",
                "make people think, don't criticize them or make them feel bad",
                "engage in way that gives the other person space to continue the conversation"
            ]
        }
    
    # Create character data structure
    character_data = {
        "name": username.lower(),
        "plugins": [],
        "clients": [],
        "modelProvider": "groq",
        "settings": {
            "secrets": {},
            "voice": {
                "model": "en_US-hfc_female-medium"
            }
        },
        "system": f"Roleplay and generate interesting content on behalf of {username}.",
        "bio": bio,
        "lore": lore,
        "knowledge": knowledge,
        "messageExamples": message_examples,
        "postExamples": post_examples,
        "adjectives": adjectives,
        "people": people,
        "topics": topics,
        "style": style
    }
    
    # Initialize file path as None
    file_path = None
    
    # Save to file if requested
    if save_file:
        # Ensure the characters directory exists
        os.makedirs("characters", exist_ok=True)
        
        # Set the file path
        file_path = os.path.join("characters", f"{username.lower()}.json")
        
        # Save the character data
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(character_data, f, indent=2)
        print(f"Character data saved to {file_path}")
    
    return character_data, file_path
result = process_character_data(
    username="techguru",
    bio=["AI researcher and tech enthusiast with a love for robotics"],
    topics=["artificial intelligence", "machine learning", "robotics"],
    post_examples=["Just spent the weekend building a neural network that generates poetry. The results are... interesting.", "Attended a conference on quantum computing today. Mind officially blown.", "Working on a new project to create a chatbot that can pass the Turing test."],
    adjectives=["technical", "thoughtful", "innovative"]
)

# Just generate the JSON without saving to a file
result = process_character_data("techguru", save_file=False)