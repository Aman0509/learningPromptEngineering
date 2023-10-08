# Expanding

| Contents |
| :--- |
| [Introduction](#introduction) |
| [Temperature of a Model](#temperature-of-a-model) |
| [Examples](#examples) |

## Introduction

Expanding in prompt engineering refers to the task of taking a brief or concise piece of text, such as instructions or a list of topics, and using a large language model to generate a longer piece of text. This extended text can be in the form of an email, essay, or any other document. The goal is to provide more detailed or comprehensive content based on the initial input.

For example, you might input a short description of a topic, and the model can expand it into a full-length article or a detailed explanation. This expansion can be valuable for various purposes, including brainstorming ideas or creating content.

However, it's important to use this capability responsibly to avoid potential misuse, such as generating spam or low-quality content. Responsible usage ensures that the generated text is helpful and meaningful to users.

## Temperature of a Model

<img src="https://drive.google.com/uc?export=view&id=13sjpECZc6WndZVfpPpfetCk_CMg12BJw" height="450" width="550" alt="DeepLearning.AI">

The "temperature" of a language model is a parameter that controls the randomness and diversity of the model's responses. It affects how the model selects the next word in its generated text.

Think of temperature as the model's level of exploration or randomness. For instance, when the phrase "my favorite food is" is given, the model's most likely next word is "pizza," followed by "sushi" and "tacos." At a temperature of zero, the model always selects the most likely next word, which, in this case, is "pizza." With a higher temperature, it may also choose one of the less likely words, and at an even higher temperature, it might even select "tacos," which has only a 5% chance of being chosen.

As the model generates more words in its response, it will increasingly diverge from the initial response. If you desire a predictable response for your applications, it is recommended to use the temperature of zero, as we have done throughout this course. However, if you want a wider range of diverse outputs for more creative purposes, a higher temperature might be preferable.

## Examples

### Customize the automated reply to a customer email

We will employ the language model to create a personalized email for a customer by considering their review and its sentiment.

```python
# given the sentiment from the lesson on "inferring",
# and the original customer message, customize the email
sentiment = "negative"

# review for a blender
review = f"""
So, they still had the 17 piece system on seasonal \
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place doesn’t look as good \
as in previous editions from a few years ago, but I \
plan to be very gentle with it (example, I crush \
very hard items like beans, ice, rice, etc. in the \ 
blender first then pulverize them in the serving size \
I want in the blender then switch to the whipping \
blade for a finer flour, and use the cross cutting blade \
first when making smoothies, then use the flat blade \
if I need them finer/less pulpy). Special tip when making \
smoothies, finely cut and freeze the fruits and \
vegetables (if using spinach-lightly stew soften the \ 
spinach then freeze until ready for use-and if making \
sorbet, use a small to medium sized food processor) \ 
that you plan to use that way you can avoid adding so \
much ice if at all-when making your smoothie. \
After about a year, the motor was making a funny noise. \
I called customer service but the warranty expired \
already, so I had to buy another one. FYI: The overall \
quality has gone done in these types of products, so \
they are kind of counting on brand recognition and \
consumer loyalty to maintain sales. Got it in about \
two days.
"""
```

```python
prompt = f"""
You are a customer service AI assistant.
Your task is to send an email reply to a valued customer.
Given the customer email delimited by ```, \
Generate a reply to thank the customer for their review.
If the sentiment is positive or neutral, thank them for \
their review.
If the sentiment is negative, apologize and suggest that \
they can reach out to customer service. 
Make sure to use specific details from the review.
Write in a concise and professional tone.
Sign the email as `AI customer agent`.
Customer review: ```{review}```
Review sentiment: {sentiment}
"""
response = get_completion(prompt)
print(response)
```

```
Output

Dear Valued Customer,

Thank you for taking the time to share your review with us. We appreciate your feedback and apologize for any inconvenience you may have experienced.

We are sorry to hear about the price increase you noticed in December. We strive to provide competitive pricing for our products, and we understand your frustration. If you have any further concerns regarding pricing or any other issues, we encourage you to reach out to our customer service team. They will be more than happy to assist you.

We also appreciate your feedback regarding the base of the system. We continuously work to improve the quality of our products, and your comments will be taken into consideration for future enhancements.

We apologize for any inconvenience caused by the motor issue you encountered. Our customer service team is always available to assist with any warranty-related concerns. We understand that the warranty had expired, but we would still like to address this matter further. Please contact our customer service team, and they will be able to provide you with further assistance.

Thank you once again for your review. We value your feedback and appreciate your loyalty to our brand. If you have any further questions or concerns, please do not hesitate to contact us.

Best regards,

AI customer agent
```

### Remind the model to use details from the customer's email (with Temperature > 0)

Here's an example of an email generated with a temperature of `0.7`, which differs from the previous email we received.

When we set the temperature to `0.7`, the generated output will vary each time you run the prompt. In contrast, with a temperature of zero, you should consistently receive the same completion.

```python
prompt = f"""
    You are a customer service AI assistant.
    Your task is to send an email reply to a valued customer.
    Given the customer email delimited by ```, \
    Generate a reply to thank the customer for their review.
    If the sentiment is positive or neutral, thank them for \
    their review.
    If the sentiment is negative, apologize and suggest that \
    they can reach out to customer service. 
    Make sure to use specific details from the review.
    Write in a concise and professional tone.
    Sign the email as `AI customer agent`.
    Customer review: ```{review}```
    Review sentiment: {sentiment}
"""
response = get_completion(prompt, temperature=0.7)
print(response)
```

```
Output

Dear Valued Customer,

Thank you for taking the time to provide your feedback on our 17 piece system. We appreciate your honest review and apologize for any inconvenience you may have experienced.

We're sorry to hear that you noticed a price increase in December compared to the seasonal sale in November. We strive to maintain competitive pricing and provide value to our customers. We apologize if this caused any frustration.

Regarding the base of the system, we appreciate your observation. We are constantly working to improve our products and will take your feedback into consideration for future enhancements.

We understand that you had a warranty issue with the motor and had to purchase another one. We apologize for any inconvenience this may have caused. If you have any further concerns or questions, please don't hesitate to reach out to our customer service team. They will be happy to assist you further.

Thank you once again for your review and for choosing our products. We value your feedback as it helps us improve our offerings.

Best regards,

AI customer agent
```