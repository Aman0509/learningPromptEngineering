from . import get_completion


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

    def tactic_two(self):
        prompt = f"""
            Generate a list of three made-up book titles along \ 
            with their authors and genres. 
            Provide them in JSON format with the following keys: 
            book_id, title, author, genre.
        """
        response = get_completion(prompt)
        print(response)

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


def model_hallucinations():
    prompt = f"""
    Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
    """
    response = get_completion(prompt)
    print(response)