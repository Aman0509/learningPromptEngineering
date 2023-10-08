# Inferring

| Contents |
| :--- |
| [Introduction](#introduction) |
| [Example](#example) |

## Introduction

In the context of prompt engineering, *inferring* refers to the process of having a large language model analyze and understand text input to perform various tasks. This can include tasks like:

1. **Extracting Labels:** Identifying specific labels or categories within a given text.
2. **Extracting Names:** Recognizing and extracting names of individuals, places, or entities from text.
3. **Sentiment Analysis:** Determining the sentiment or emotional tone conveyed by a piece of text, such as whether it's positive, negative, or neutral.
4. **Other Types of Analysis:** Performing various types of text analysis, such as identifying keywords, summarizing content, or extracting specific information.

In the traditional machine learning process, accomplishing something like sentiment analysis required collecting labeled datasets, training a model, deploying it in the cloud, and making inferences. While this method can work effectively, it involves a lot of effort, especially when dealing with various tasks like sentiment analysis, name extraction, and others, as each task requires a separate model.

A significant advantage of large language models is that, for many of these tasks, you can simply provide a prompt and get results quickly, streamlining application development. Additionally, you can use a single model and API for multiple tasks instead of having to train and deploy numerous different models.

## Example

By using below review, we'll try to infer different things.

```python
lamp_review = """
    Needed a nice lamp for my bedroom, and this one had \
    additional storage and not too high of a price point. \
    Got it fast.  The string to our lamp broke during the \
    transit and the company happily sent over a new one. \
    Came within a few days as well. It was easy to put \
    together.  I had a missing part, so I contacted their \
    support and they very quickly got me the missing piece! \
    Lumina seems to me to be a great company that cares \
    about their customers and products!!
"""
```

***Sentiment Classification (Positive/Negative)***

```python
prompt = f"""
    What is the sentiment of the following product review, 
    which is delimited with triple backticks?

    Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

```
Output

The sentiment of the product review is positive.
```

Output seems pretty right. This lamp isn't perfect, but the customer seems pretty happy. Seems to be a great company that cares about the customers and products.

However, if someone prefer a shorter and more straightforward response, we can modify this prompt by adding an instruction to provide brief, one-word answers that are either positive or negative like below.

```python
prompt = f"""
    What is the sentiment of the following product review, 
    which is delimited with triple backticks?

    Give your answer as a single word, either "positive" \
    or "negative".

    Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

```
Output

positive
```

***Identify types of Emotions***

```python
prompt = f"""
    Identify a list of emotions that the writer of the \
    following review is expressing. Include no more than \
    five items in the list. Format your answer as a list of \
    lower-case words separated by commas.

    Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

```
Output

satisfied, pleased, grateful, impressed, happy
```

***Identify Anger***

Let's say you are specifically looking to find if review has any anger sentiments.

```python
prompt = f"""
    Is the writer of the following review expressing anger?\
    The review is delimited with triple backticks. \
    Give your answer as either yes or no.

    Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

```
Output

No
```

***Extract Product and Company name from Customer Reviews***

Let's explore more capabilities of this system, particularly in extracting richer information from customer reviews. Information extraction, a component of Natural Language Processing (NLP), involves extracting specific details from text. In this prompt, we instruct it to identify two things: **the purchased item and the manufacturer's name.** When dealing with a large number of reviews from an e-commerce website, you might find it valuable to extract such information from your extensive review collection. This can help you identify the products, their manufacturers, gauge sentiment, and track trends in sentiment for specific items or brands. In this example, we'll request the response to be formatted as a JSON object with "Item" and "Brand" as the keys.

```python
prompt = f"""
    Identify the following items from the review text: 
    - Item purchased by reviewer
    - Company that made the item

    The review is delimited with triple backticks. \
    Format your response as a JSON object with \
    "Item" and "Brand" as the keys. 
    If the information isn't present, use "unknown" \
    as the value.
    Make your response as short as possible.
    
    Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

```json
{
  "Item": "lamp",
  "Brand": "Lumina"
}
```

***Doing multiple tasks at once***

Above discussed examples can be packed into a single prompt like below:

```python
prompt = f"""
    Identify the following items from the review text: 
    - Sentiment (positive or negative)
    - Is the reviewer expressing anger? (true or false)
    - Item purchased by reviewer
    - Company that made the item

    The review is delimited with triple backticks. \
    Format your response as a JSON object with \
    "Sentiment", "Anger", "Item" and "Brand" as the keys.
    If the information isn't present, use "unknown" \
    as the value.
    Make your response as short as possible.
    Format the Anger value as a boolean.

    Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)
```

```json
{
  "Sentiment": "positive",
  "Anger": false,
  "Item": "lamp",
  "Brand": "Lumina"
}
```

***Inferring Topics***

One interesting use case of large language models is topic inference. When presented with a lengthy text, these models can determine what the text is primarily focused on and identify its key subjects or themes.

Let's take an example:

```python
story = """
    In a recent survey conducted by the government, 
    public sector employees were asked to rate their level 
    of satisfaction with the department they work at. 
    The results revealed that NASA was the most popular 
    department with a satisfaction rating of 95%.

    One NASA employee, John Smith, commented on the findings, 
    stating, "I'm not surprised that NASA came out on top. 
    It's a great place to work with amazing people and 
    incredible opportunities. I'm proud to be a part of 
    such an innovative organization."

    The results were also welcomed by NASA's management team, 
    with Director Tom Johnson stating, "We are thrilled to 
    hear that our employees are satisfied with their work at NASA. 
    We have a talented and dedicated team who work tirelessly 
    to achieve our goals, and it's fantastic to see that their 
    hard work is paying off."

    The survey also revealed that the 
    Social Security Administration had the lowest satisfaction 
    rating, with only 45% of employees indicating they were 
    satisfied with their job. The government has pledged to 
    address the concerns raised by employees in the survey and 
    work towards improving job satisfaction across all departments.
"""
```

Based on above story, let's ask LLM to infer 5 topics,

```python
prompt = f"""
    Determine five topics that are being discussed in the \
    following text, which is delimited by triple backticks.

    Make each item one or two words long. 

    delimit your response by comma.

    Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)
```

```
Output

survey, satisfaction, NASA, Social Security Administration, job satisfaction
```

***Make a news alert for certain topics***

Let's take different topics

```python
topic_list = [
    "nasa", "local government", "engineering", 
    "employee satisfaction", "federal government"
]
```

Now, we will check which of these topics covered in our previous article

```python
prompt = f"""
    Determine whether each item in the following list of \
    topics is a topic in the text below, which
    is delimited with triple backticks.

    Give your answer as normal list separated with ':' with 0 or 1 for each topic.\

    List of topics: {", ".join(topic_list)}

    Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)
```

```
Output

nasa: 1
local government: 0
engineering: 0
employee satisfaction: 1
federal government: 1
```

This is sometimes called as "Zero-Shot Learning Algorithm" in machine learning. It's called "Zero-Shot" because it didn't rely on any labeled training data. Simply by using a prompt, it managed to identify the topics discussed in the news article.

```python
# Create Alert for NASA
topic_dict = {i.split(': ')[0]: int(i.split(': ')[1]) for i in response.split(sep='\n')}
if topic_dict['nasa'] == 1:
    print("ALERT: New NASA story!")
```

```
Output

ALERT: New NASA story!
```
