import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


# helper function
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


class PrincipleOne:
    def tactic_one(self):
        text = f"""
                You should express what you want a model to do by \ 
                providing instructions that are as clear and \ 
                specific as you can possibly make them. \ 
                This will guide the model towards the desired output, \ 
                and reduce the chances of receiving irrelevant \ 
                or incorrect responses. Don't confuse writing a \ 
                clear prompt with writing a short prompt. \ 
                In many cases, longer prompts provide more clarity \ 
                and context for the model, which can lead to \ 
                more detailed and relevant outputs.
                """
        prompt = f"""
        Summarize the text delimited by triple backticks \ 
        into a single sentence.
        ```{text}```
        """
        response = get_completion(prompt)
        print(response)

        """
        Output:
        To guide a model towards the desired output and reduce irrelevant or incorrect responses, it is important to provide clear and specific instructions, which can be achieved through longer prompts that offer more clarity and context.
        """

    def tactic_two(self):
        prompt = f"""
            Generate a list of three made-up book titles along \ 
            with their authors and genres. 
            Provide them in JSON format with the following keys: 
            book_id, title, author, genre.
        """
        response = get_completion(prompt)
        print(response)

        """
        Output:
        {
            "books": [
                {
                "book_id": 1,
                "title": "The Enigma of Elysium",
                "author": "Evelyn Sinclair",
                "genre": "Mystery"
                },
                {
                "book_id": 2,
                "title": "Whispers in the Wind",
                "author": "Nathaniel Blackwood",
                "genre": "Fantasy"
                },
                {
                "book_id": 3,
                "title": "Echoes of the Past",
                "author": "Amelia Hart",
                "genre": "Romance"
                }
            ]
        }
        """

    def tactic_three(self):
        text_1 = f"""
            Making a cup of tea is easy! First, you need to get some \ 
            water boiling. While that's happening, \ 
            grab a cup and put a tea bag in it. Once the water is \ 
            hot enough, just pour it over the tea bag. \ 
            Let it sit for a bit so the tea can steep. After a \ 
            few minutes, take out the tea bag. If you \ 
            like, you can add some sugar or milk to taste. \ 
            And that's it! You've got yourself a delicious \ 
            cup of tea to enjoy.
        """
        text_2 = f"""
            The sun is shining brightly today, and the birds are \
            singing. It's a beautiful day to go for a \ 
            walk in the park. The flowers are blooming, and the \ 
            trees are swaying gently in the breeze. People \ 
            are out and about, enjoying the lovely weather. \ 
            Some are having picnics, while others are playing \ 
            games or simply relaxing on the grass. It's a \ 
            perfect day to spend time outdoors and appreciate the \ 
            beauty of nature.
        """
        c = 1
        for t in (text_1, text_2):
            prompt = f"""
                You will be provided with text delimited by triple quotes. 
                If it contains a sequence of instructions, \ 
                re-write those instructions in the following format:

                Step 1 - ...
                Step 2 - …
                …
                Step N - …

                If the text does not contain a sequence of instructions, \ 
                then simply write \"No steps provided.\"

                \"\"\"{t}\"\"\"
            """
            response = get_completion(prompt)
            print(f"Output - {c}")
            print(response)
            print()
            c += 1

        """
        Output:
        Output - 1
        Step 1 - Get some water boiling.
        Step 2 - Grab a cup and put a tea bag in it.
        Step 3 - Once the water is hot enough, pour it over the tea bag.
        Step 4 - Let it sit for a bit so the tea can steep.
        Step 5 - After a few minutes, take out the tea bag.
        Step 6 - If you like, add some sugar or milk to taste.
        Step 7 - Enjoy your delicious cup of tea.

        Output - 2
        No steps provided.
        """

    def tactic_four(self):
        prompt = f"""
            Your task is to answer in a consistent style.

            <child>: Teach me about patience.

            <grandparent>: The river that carves the deepest \ 
            valley flows from a modest spring; the \ 
            grandest symphony originates from a single note; \ 
            the most intricate tapestry begins with a solitary thread.

            <child>: Teach me about resilience.
        """
        response = get_completion(prompt)
        print(response)

        """
        Output:
        <grandparent>: Resilience is like a mighty oak tree that withstands the strongest storms, bending but never breaking. It is the unwavering determination to rise again after every fall, and the ability to find strength in the face of adversity. Just as a diamond is formed under immense pressure, resilience is forged through challenges and hardships, making us stronger and more resilient in the process.
        """


class PrincipleTwo:
    def tactic_one(self):
        text = f"""
            In a charming village, siblings Jack and Jill set out on \ 
            a quest to fetch water from a hilltop \ 
            well. As they climbed, singing joyfully, misfortune \ 
            struck—Jack tripped on a stone and tumbled \ 
            down the hill, with Jill following suit. \ 
            Though slightly battered, the pair returned home to \ 
            comforting embraces. Despite the mishap, \ 
            their adventurous spirits remained undimmed, and they \ 
            continued exploring with delight.
        """

        prompt_1 = f"""
            Perform the following actions: 
            1 - Summarize the following text delimited by triple \
            backticks with 1 sentence.
            2 - Translate the summary into French.
            3 - List each name in the French summary.
            4 - Output a json object that contains the following \
            keys: french_summary, num_names.

            Separate your answers with line breaks.

            Text:
            ```{text}```
        """
        response = get_completion(prompt_1)
        print("Completion for prompt 1:")
        print(response)

        """
        Output:
        Completion for prompt 1:
        1 - Jack and Jill, siblings, go on a quest to fetch water from a hilltop well, but encounter misfortune when Jack trips on a stone and tumbles down the hill, with Jill following suit, yet they return home and remain undeterred in their adventurous spirits.

        2 - Jack et Jill, frère et sœur, partent en quête d'eau d'un puits au sommet d'une colline, mais rencontrent un malheur lorsque Jack trébuche sur une pierre et dévale la colline, suivi par Jill, pourtant ils rentrent chez eux et restent déterminés dans leur esprit d'aventure.

        3 - Jack, Jill

        4 - {
        "french_summary": "Jack et Jill, frère et sœur, partent en quête d'eau d'un puits au sommet d'une colline, mais rencontrent un malheur lorsque Jack trébuche sur une pierre et dévale la colline, suivi par Jill, pourtant ils rentrent chez eux et restent déterminés dans leur esprit d'aventure.",
        "num_names": 2
        }
        """

    def tactic_two(self):
        prompt = f"""
            Determine if the student's solution is correct or not.

            Question:
            I'm building a solar power installation and I need \
            help working out the financials. 
            - Land costs $100 / square foot
            - I can buy solar panels for $250 / square foot
            - I negotiated a contract for maintenance that will cost \ 
            me a flat $100k per year, and an additional $10 / square \
            foot
            What is the total cost for the first year of operations 
            as a function of the number of square feet.

            Student's Solution:
            Let x be the size of the installation in square feet.
            Costs:
            1. Land cost: 100x
            2. Solar panel cost: 250x
            3. Maintenance cost: 100,000 + 100x
            Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
        """
        response = get_completion(prompt)
        print(response)

        """
        Output:
        The student's solution is correct. They correctly identified the costs for land, solar panels, and maintenance, and calculated the total cost for the first year of operations as a function of the number of square feet.
        """


def model_hallucinations():
    prompt = f"""
    Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
    """
    response = get_completion(prompt)
    print(response)

    """
    Output:
    The AeroGlide UltraSlim Smart Toothbrush by Boie is a technologically advanced toothbrush designed to provide a superior brushing experience. Boie is a company known for its innovative oral care products, and the AeroGlide UltraSlim Smart Toothbrush is no exception.

    One of the standout features of this toothbrush is its ultra-slim design. The brush head is only 2mm thick, making it much thinner than traditional toothbrushes. This slim profile allows for better access to hard-to-reach areas of the mouth, ensuring a thorough and effective clean.

    The AeroGlide UltraSlim Smart Toothbrush also incorporates smart technology. It connects to a mobile app via Bluetooth, allowing users to track their brushing habits and receive personalized recommendations for improving their oral hygiene routine. The app provides real-time feedback on brushing technique, duration, and coverage, helping users to achieve optimal oral health.

    The toothbrush features soft, antimicrobial bristles that are gentle on the gums and teeth. These bristles are also infused with silver, which helps to inhibit the growth of bacteria on the brush head. This ensures a clean and hygienic brushing experience every time.

    In addition to its advanced features, the AeroGlide UltraSlim Smart Toothbrush is also eco-friendly. It is made from a durable thermoplastic elastomer material that is 100% recyclable. This makes it a sustainable choice for those who are conscious of their environmental impact.

    Overall, the AeroGlide UltraSlim Smart Toothbrush by Boie offers a combination of advanced technology, superior design, and eco-friendliness. It is a great option for individuals looking to upgrade their oral care routine and achieve optimal oral health.
    """
