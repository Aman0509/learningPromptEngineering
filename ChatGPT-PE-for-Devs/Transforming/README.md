# Transforming

| Contents |
| :--- |
| [Introduction](#introduction) |
| [Translation](#translation) |
| [Universal Translator](#universal-translator) |
| [Tone Transformation](#tone-transformation) |
| [Format Conversion](#format-conversion) |
| [Spellcheck/Grammar check](#spellcheckgrammar-check) |

## Introduction

Transforming in Prompt Engineering refers to the capability of large language models to convert input text from one format or language into another. This transformation can involve several tasks, such as:

1. **Language Translation:** Converting text from one language to another. For example, translating English text into French or vice versa.

2. **Spelling and Grammar Correction:** Assisting in rectifying errors in spelling and grammar within the input text.

3. **Format Conversion:** Changing the format of text from one structure to another. For instance, converting HTML code into JSON format.

This ability to transform text is highly valuable for automating various language-related tasks, making them more efficient and accurate. Large language models can handle these transformations effectively, reducing the need for manual coding and regular expressions for such tasks.

## Translation

Large language models are trained using vast amounts of text data, which often includes internet content in numerous languages. This extensive training equips the model with the capability to perform translation tasks. These models possess knowledge of hundreds of languages with varying levels of proficiency.

Let's see some examples:

```python
prompt = f"""
    Translate the following English text to Spanish: \ 
    ```Hi, I would like to order a blender```
"""
response = get_completion(prompt)
print(response)
```

```
Output

Hola, me gustaría ordenar una licuadora.
```

```python
prompt = f"""
    Tell me which language this is: 
    ```Combien coûte le lampadaire?```
"""
response = get_completion(prompt)
print(response)
```

```
Output

This language is French.
```

```python
prompt = f"""
    Translate the following  text to French and Spanish
    and English Pirate: \
    ```I want to order a basketball```
"""
response = get_completion(prompt)
print(response)
```

```
Output

French: ```Je veux commander un ballon de basket```
Spanish: ```Quiero ordenar una pelota de baloncesto```
English Pirate: ```I be wantin' to order a basketball```
```

```python
prompt = f"""
    Translate the following text to Spanish in both the \
    formal and informal forms: 
    'Would you like to order a pillow?'
"""
response = get_completion(prompt)
print(response)
```

```
Output

Formal: ¿Le gustaría ordenar una almohada?
Informal: ¿Te gustaría ordenar una almohada?
```

## Universal Translator

Imagine you are in charge of IT at a large multinational e-commerce company. Users are messaging you with IT issues in all their native languages. Your staff is from all over the world and speaks only their native languages. You need a universal translator!

```python
user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
]

for issue in user_messages:
    prompt = f"Tell me what language this is: ```{issue}```"
    lang = get_completion(prompt)
    print(f"Original message ({lang}): {issue}")

    prompt = f"""
    Translate the following  text to English \
    and Korean: ```{issue}```
    """
    response = get_completion(prompt)
    print(response, "\n")
```

```
Output

Original message (The language is French.): La performance du système est plus lente que d'habitude.
The performance of the system is slower than usual.

시스템의 성능이 평소보다 느립니다. 

Original message (The language is Spanish.): Mi monitor tiene píxeles que no se iluminan.
English: "My monitor has pixels that do not light up."

Korean: "내 모니터에는 밝아지지 않는 픽셀이 있습니다." (Nae moniteoeneun balkaji-ji anhneun piksel-i issseumnida.) 

Original message (The language is Italian.): Il mio mouse non funziona
English: "My mouse is not working."
Korean: "내 마우스가 작동하지 않습니다." 

Original message (The language is Polish.): Mój klawisz Ctrl jest zepsuty
English: "My Ctrl key is broken"
Korean: "내 Ctrl 키가 고장 났어요" 

Original message (The language is Chinese.): 我的屏幕在闪烁
English: My screen is flickering.
Korean: 내 화면이 깜박거립니다. 
```

## Tone Transformation

Writing can vary based on the intended audience. ChatGPT can produce different tones.

```python
prompt = f"""
    Translate the following from slang to a business letter: 
    'Dude, This is Joe, check out this spec on this standing lamp.'
"""
response = get_completion(prompt)
print(response)
```

```
Output

Dear Sir/Madam,

I hope this letter finds you well. My name is Joe, and I am writing to bring your attention to a specification document regarding a standing lamp. 

I kindly request that you take a moment to review the attached spec, as it contains important details about the standing lamp in question. 

Thank you for your time and consideration. I look forward to hearing from you soon.

Sincerely,
Joe
```

## Format Conversion

ChatGPT can translate between formats. The prompt should describe the input and output formats.

```python
data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

prompt = f"""
    Translate the following python dictionary from JSON to an HTML \
    table with column headers and title: {data_json}
"""
response = get_completion(prompt)
print(response)
```

```HTML
Output

<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Restaurant Employees</h2>

<table>
  <tr>
    <th>Name</th>
    <th>Email</th>
  </tr>
  <tr>
    <td>Shyam</td>
    <td>shyamjaiswal@gmail.com</td>
  </tr>
  <tr>
    <td>Bob</td>
    <td>bob32@gmail.com</td>
  </tr>
  <tr>
    <td>Jai</td>
    <td>jai87@gmail.com</td>
  </tr>
</table>

</body>
</html>
```

<img src="https://drive.google.com/uc?export=view&id=1UG1pNLnQhikDrI0FIOW58tByMqBf_1kc" alt="DeepLearning.AI">

## Spellcheck/Grammar check

To signal to the LLM that you want it to proofread your text, you instruct the model to 'proofread' or 'proofread and correct'.

Here are some examples of common grammar and spelling problems and the LLM's response.

Example 1:

```python
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for speling abilitty"  # spelling
]
for t in text:
    prompt = f"""
        Proofread and correct the following text
        and rewrite the corrected version. If you don't find
        and errors, just say "No errors found". Don't use 
        any punctuation around the text:
        ```{t}```
    """
    response = get_completion(prompt)
    print(response)
```

```
Output

The girl with the black and white puppies has a ball.
No errors found.
It's going to be a long day. Does the car need its oil changed?
There goes my freedom. They're going to bring their suitcases.
You're going to need your notebook.
That medicine affects my ability to sleep. Have you heard of the butterfly effect?
This phrase is to check chatGPT for spelling ability.
```

Example 2:

```python
text = f"""
    Got this for my daughter for her birthday cuz she keeps taking \
    mine from my room.  Yes, adults also like pandas too.  She takes \
    it everywhere with her, and it's super soft and cute.  One of the \
    ears is a bit lower than the other, and I don't think that was \
    designed to be asymmetrical. It's a bit small for what I paid for it \
    though. I think there might be other options that are bigger for \
    the same price.  It arrived a day earlier than expected, so I got \
    to play with it myself before I gave it to my daughter.
"""
prompt = f"proofread and correct this review: ```{text}```"
response = get_completion(prompt)
print(response)
```

```
Output

Got this for my daughter for her birthday because she keeps taking mine from my room. Yes, adults also like pandas too. She takes it everywhere with her, and it's super soft and cute. However, one of the ears is a bit lower than the other, and I don't think that was designed to be asymmetrical. Additionally, it's a bit small for what I paid for it. I believe there might be other options that are bigger for the same price. On the positive side, it arrived a day earlier than expected, so I got to play with it myself before I gave it to my daughter.
```

Example 3:

```python
prompt = f"""
    proofread and correct this review. Make it more compelling. 
    Ensure it follows APA style guide and targets an advanced reader. 
    Output in markdown format.
    Text: ```{text}```
"""
response = get_completion(prompt)
print(response)
```

```
Output

**Review of a Panda Plush Toy: A Perfect Gift for All Ages**

I purchased this delightful panda plush toy as a birthday gift for my daughter, who has a penchant for "borrowing" my belongings from my room. However, it turns out that adults can also find joy in the company of these adorable creatures. 

The moment my daughter received this gift, she instantly fell in love with it. Its irresistibly soft and cuddly texture makes it the perfect companion for her daily adventures. However, I did notice a slight asymmetry in the placement of the ears, which I believe was unintentional. Nonetheless, this minor flaw does not detract from the overall charm of the toy.

While the quality and cuteness of the panda plush are undeniable, I must admit that I found its size to be slightly smaller than expected, considering its price. It would be beneficial for potential buyers to explore alternative options that offer a larger size for the same price point.

On a positive note, the delivery of the product exceeded my expectations. It arrived a day earlier than anticipated, allowing me to indulge in some playtime with the panda plush before presenting it to my daughter. This unexpected bonus added to the overall satisfaction of the purchase.

In conclusion, this panda plush toy is a delightful gift that transcends age boundaries. Its softness and charm make it an irresistible companion for anyone seeking comfort and cuteness. While the size may not meet everyone's expectations, the joy it brings is immeasurable. With prompt delivery and exceptional quality, this panda plush toy is a worthwhile investment for those seeking a unique and endearing gift.
```
