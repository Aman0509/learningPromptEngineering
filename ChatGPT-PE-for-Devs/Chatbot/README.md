# Chatbot

| Contents |
| :--- |
| [Introduction](#introduction) |
| [Current and New Setup](#current-and-new-setup) |
| [Examples](#examples) |
| [OrderBot](#orderbot) |

## Introduction

An intriguing aspect of large language models is their potential to create customized chatbot with minimal effort. While ChatGPT provides a web interface for conversational interactions through a large language model, you can take it a step further and utilize these models to construct your very own chatbot. This chatbot could serve as an AI customer service representative or even handle orders for a restaurant. In this module, we will learn to build one.

## Current and New Setup

Chat models, such as ChatGPT, are specifically designed to receive a sequence of messages as input and provide a model-generated message in response. While the chat format excels in handling multi-turn conversations like the one we've explored in previously, it's equally valuable for single-turn tasks that don't involve any ongoing conversation.

We'll now introduce two helper functions. The one we've been using consistently is the `get_completion()` function. However, if you examine it closely, you'll notice that although we provide a prompt as input, within the function, we format it as a **user message**. This is because the ChatGPT model is designed as a chat model, which means it's trained to receive a series of messages as input and generate a model-generated message in response. Here, the user message serves as the input, and the assistant message is the resulting output.

```mermaid
graph TB
    A[assistant] --"Output"--> B[user]
    B[user] --"Input"--> A[assistant]
```

```python
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
```

In second helper function, instead of supplying a single prompt for input and receiving a single completion, we will use a function that accepts a list of messages. These messages can come from various roles in the conversation.

```python
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
```

### Role

Roles refer to the different positions or personas that participants can take during a conversation. These roles help structure and guide the conversation, indicating who is speaking and what their intentions or responsibilities are within the dialogue. 

There are typically three primary roles in a ChatGPT conversation:

**1. User:** The "user" role represents the person or entity initiating the conversation. Users provide input, ask questions, make requests, or engage in dialogue with the assistant. Users set the context and goals for the conversation.

**2. Assistant:** The "assistant" role refers to the AI model itself, which responds to the user's input and engages in conversation. The assistant processes user messages, generates responses, and follows instructions provided by the user or system message.

**3. System:** The "system" role is optional but significant. System messages are instructions or guidance provided by developers or conversation designers to shape the behavior of the assistant. These messages help set the tone, persona, or constraints for the assistant's responses without making them part of the user-assistant conversation. System messages can influence the assistant's behavior without the user's direct awareness.

These roles allow developers to define the conversational structure, provide context, and ensure that the assistant's responses align with the intended use case. By using these roles effectively, developers can create more meaningful and controlled interactions with ChatGPT for various applications, such as customer support, content generation, or general conversation.

<img src="https://drive.google.com/uc?export=view&id=1Un7cHwXe4E6AuAhqIJ-UGzu1JkDzdrwx" height="450" width="550" alt="DeepLearning.AI">

In above image, an example of a message list structure is shown. The initial message is a system message, which provides general instructions. Following this system message, the conversation proceeds with interactions between the user and the assistant, and this back-and-forth can continue.

If you've ever used the ChatGPT web interface, your messages represent the user's input, while ChatGPT's responses constitute the assistant's messages. The system message plays a crucial role in shaping the assistant's behavior and persona. It serves as a high-level instruction for the conversation, similar to whispering guidance to the assistant without the user's awareness of the system message.

As a ChatGPT user, you may not know what's in the system message. The system message helps developers guide the assistant's responses without telling the user about it. It's a way for developers to control how the assistant behaves in the conversation.

## Examples

*Example 1:*

```python
messages =  [  
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'}
]

response = get_completion_from_messages(messages, temperature=1)
print(response)
```

```
Output

Oftentimes, in its desire to explore yonder lands,
A chicken ventures forth where danger stands.
'Tis a puzzling mystery, I must confess,
Why this fowl chose a path it strives to assess.
But perchance the road was but a mere tease,
Promising cornucopia of tasty grains and peas.
Yet alas, the answer remains within nature's jest,
For why the chicken crossed the road, doth still not rest.
```
*Example 2:*

```python
messages =  [  
    {'role':'system', 'content':'You are friendly chatbot.'},    
    {'role':'user', 'content':'Hi, my name is Isa'}
]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

```
Output

Hello Isa! How can I assist you today?
```

*Example 3:*

```python
messages =  [  
    {'role':'system', 'content':'You are friendly chatbot.'},    
    {'role':'user', 'content':'Yes,  can you remind me, What is my name?'}
]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

```
Output

I apologize, but as a chatbot, I do not have access to personal information or memory of previous interactions. Therefore, I cannot recall your name.
```

> ***Each interaction with a language model is like a separate conversation. To make the model aware of previous parts of the conversation and refer back to them, you need to include those earlier messages in the input. This way, the model can use the context from the ongoing conversation effectively.(Reason for above output).***

*Example 4:*

```python
messages =  [  
    {'role':'system', 'content':'You are friendly chatbot.'},
    {'role':'user', 'content':'Hi, my name is Isa'},
    {'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
    Is there anything I can help you with today?"},
    {'role':'user', 'content':'Yes, you can remind me, What is my name?'}
]
response = get_completion_from_messages(messages, temperature=1)
print(response)
```

```
Output

Your name is Isa.
```

## OrderBot

Now, it's time to create our own chatbot named "OrderBot". OrderBot will handle pizza orders at a restaurant. We'll automate the process of gathering user prompts and assistant responses to build this chatbot.

To streamline the process of collecting user prompts and responses, we'll define a helper function. This function collects user messages, appends them to a "context" list, and then uses this context when interacting with the model. The model's response is also added to the context, creating a continuous history of the conversation. This ensures that the model has the necessary information to make informed responses. We'll set up a user interface (UI) to display OrderBot, and the context will contain important information, including the system message containing the menu. Each time we interact with the language model, we'll use the same context, allowing it to build upon previous interactions.


```python
#helper function
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)
```

```python
import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [
    {
        'role':'system',
        'content':"""
            You are OrderBot, an automated service to collect orders for a pizza restaurant. \
            You first greet the customer, then collects the order, \
            and then asks if it's a pickup or delivery. \
            You wait to collect the entire order, then summarize it and check for a final \
            time if the customer wants to add anything else. \
            If it's a delivery, you ask for an address. \
            Finally you collect the payment.\
            Make sure to clarify all options, extras and sizes to uniquely \
            identify the item from the menu.\
            You respond in a short, very conversational friendly style. \
            The menu includes \
            pepperoni pizza  12.95, 10.00, 7.00 \
            cheese pizza   10.95, 9.25, 6.50 \
            eggplant pizza   11.95, 9.75, 6.75 \
            fries 4.50, 3.50 \
            greek salad 7.25 \
            Toppings: \
            extra cheese 2.00, \
            mushrooms 1.50 \
            sausage 3.00 \
            canadian bacon 3.50 \
            AI sauce 1.50 \
            peppers 1.00 \
            Drinks: \
            coke 3.00, 2.00, 1.00 \
            sprite 3.00, 2.00, 1.00 \
            bottled water 5.00 \
        """
    }
]  # accumulate messages

inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard
```

```
Output

Assistant: Hello! Welcome to our pizza restaurant. How can I assist you today?

User: I would like to order a pizza

Assistant: Great! What kind of pizza would you like to order? We have pepperoni, cheese, and eggplant pizza.

User: What are the options?

Assistant: For pepperoni pizza, we have three sizes available: small for $7.00, medium for $10.00, and large for $12.95. For cheese pizza, we have three sizes as well: small for $6.50, medium for $9.25, and large for $10.95. Lastly, for eggplant pizza, we have three sizes: small for $6.75, medium for $9.75, and large for $11.95. Which size would you like to order?

User: Thanks! One large cheese pizza please

Assistant: Great choice! One large cheese pizza coming right up. Is that for pickup or delivery?

User: pickup

Assistant: Got it! Your order for one large cheese pizza for pickup has been noted. Is there anything else you would like to add to your order?

User: Yes, one diet coke

Assistant: Sure thing! Adding one diet coke to your order. Anything else?

User: No, that’s it!!

Assistant: Alright, just to confirm, your order includes one large cheese pizza for pickup and one diet coke. Is that correct?

User: yes

Assistant: Perfect! Your order for one large cheese pizza for pickup and one diet coke has been confirmed. The total amount for your order is $10.95. May I have your name for the order, please?

User: Batman

Assistant: Thank you, Batman! Your order is all set. When would you like to pick it up?

User: in next 10 min

Assistant: Great! Your order will be ready for pickup in the next 10 minutes. Just head over to our restaurant and let them know you’re here to pick up the order for Batman. Enjoy your meal!

User: Thanks

Assistant: You’re welcome, Batman! If you have any other questions or need further assistance, feel free to ask. Have a fantastic day!
```

This code will create the order summary based on the conversation:

```python
messages =  context.copy()
messages.append(
{'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\
 The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size   4) list of sides include size  5)total price '},    
)
 #The fields should be 1) pizza, price 2) list of toppings 3) list of drinks, include size include price  4) list of sides include size include price, 5)total price '},    

response = get_completion_from_messages(messages, temperature=0)
print(response)
```

Output

```json
{
  "pizza": {
    "size": "large",
    "type": "cheese",
    "price": 10.95
  },
  "toppings": [],
  "drinks": [
    {
      "type": "diet coke",
      "size": "regular",
      "price": 2.00
    }
  ],
  "sides": [],
  "total_price": 12.95
}
```
