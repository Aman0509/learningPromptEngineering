# Introduction to Prompt Engineering

| Contents |
| :--- |
| [Brief on Artificial Intelligence](#brief-on-artificial-intelligence) |
| [Brief on Generative AI](#brief-on-generative-ai) |
| [Two Types of Large Language Models (LLMs)](#two-types-of-large-language-models-llms) |
| [What is Prompt Engineering?](#what-is-prompt-engineering) |
| [Why Prompt Engineering?](#why-prompt-engineering) |

## Brief on Artificial Intelligence

<img src="https://drive.google.com/uc?export=view&id=18lClVtYnRpX_DkKM5xzFhqSi0gcfjFcs" height="350" width="700" alt="PW Skills Tech">

It's important to know that machine learning and deep learning are like building blocks of artificial intelligence (AI). Even if you're not familiar with all the technical details, the main aim is to create AI applications. In simple terms, AI includes everything related to these areas.

Now, let's talk about machine learning. Machine learning is a part of AI. It gives you tools to train custom models for specific tasks, like predicting or sorting things in data. It uses math to help with tasks such as categorizing, predicting, and even making forecasts with different types of data.

Deep learning is a type of machine learning. People have been thinking about it since the 1950s, wondering if computers can learn like humans. This led to the idea of neural networks. Deep learning uses these multi-layered networks to do tasks like sorting, predicting, and understanding things in data, especially when there's a lot of data to work with.

In deep learning, we explore interesting ideas like artificial neural networks, Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), which can work bidirectionally and remember information over time using LSTM networks. We also look at things like auto encoders, encoders, decoders, and Transformers. These are central to various tasks in natural language processing (NLP), like understanding sentiment, creating chatbots, summarizing text, and more.

Now, let's zoom in on deep learning and talk about two main areas. First, there's something called 'generative AI,' which is part of deep learning. In generative AI, the goal is to build models that can create new content on their own, whether it's images or text. These models take input and make entirely new stuff. A specific type of model in generative AI is the 'Large Language Model' or 'LLM,' which is used to generate text. There are many other deep learning techniques, but these are the core ideas which is good for introduction purpose. Now, let's see how generative AI and LLMs fit into the bigger world of deep learning and AI.

**Readings/Sources:**

- [What is Generative AI And Prompt Engineering By Krish Naik - PW Skills Tech](https://www.youtube.com/watch?v=n7b9cbkj0_I)

## Brief on Generative AI

<img src="https://drive.google.com/uc?export=view&id=1_oxUbMLb03TTg51LZuTNdBuTyv1LXg7Q" height="350" width="700" alt="PW Skills Tech">

In deep learning, we have two main types of techniques: **Discriminative AI** and **Generative AI**. Discriminative AI is quite common, and it includes methods like artificial neural networks, **Convolutional Neural Networks** (CNNs), **Recurrent Neural Networks (RNNs)**, and Transformers. These techniques are used to solve specific problems, such as text summarization, language translation, or sentiment analysis. When we talk about discriminative AI, we often mean supervised learning, where models are trained with a lot of data to solve particular tasks.

On the other hand, generative AI is gaining popularity. In generative AI, we use techniques like **Generative Adversarial Networks (GANs)** and **Auto Encoders**. These models can create new content based on what they've learned from existing data. For example, they can generate new text or images. Some well-known generative AI models are GPT-3.5, GPT-4.0, and Google's PaLM 2 models. These are called **Large Language Models (LLMs)** because they've been trained on massive amounts of data and fine-tuned to generate accurate responses.

Generative AI, especially LLMs, is becoming popular because it offers high accuracy without the need to train models from scratch. Companies like OpenAI provide APIs for these models, making them accessible and customizable for various industries and applications. For instance, you can use them to create chatbots tailored to specific domains like healthcare, finance, or e-commerce.

> *One essential aspect of working with LLMs is 'Prompt Engineering', which involves crafting effective instructions or prompts to get the desired responses from the model.*

**Readings/Sources:**

- [What is Generative AI And Prompt Engineering By Krish Naik - PW Skills Tech](https://www.youtube.com/watch?v=n7b9cbkj0_I)

## Two Types of Large Language Models (LLMs)

<img src="https://drive.google.com/uc?export=view&id=1dowgtyoosMEd11GbEgmaYbg3KCMipyC1" alt="DeepLearning.AI">

In the realm of developing large language models, often referred to as LLMs, there are essentially two main categories: **Base LLMs** and **Instruction-Tuned LLMs**. Let's delve into these distinctions:

A ***Base LLM*** undergoes training to predict the next word in a sequence based on extensive text training data. This data is typically sourced from a wide range of internet and other textual sources. The aim here is to deduce the most probable word to follow in a given context.

For instance, if you were to provide it with the prompt

```
Once upon a time there was a unicorn,
```
it might complete the sentence with something like:

```
that lived in a magical forest with all unicorn friends.
```

However, if you were to ask a factual question like:

```
What is the capital of France?
```

the base LLM might respond with a more factual and information-based answer, such as,

```
What is France's largest city? OR
What is France's population?
```

This is because it tends to generate responses based on the patterns it has learned from various internet articles, which often contain lists of factual questions.

On the other hand, an ***Instruction-tuned LLM*** is where a significant portion of LLM research and application development has been concentrated. An instruction-tuned LLM is trained to follow explicit instructions.

For example, if you ask it,

```
What is the capital of France?
```

it is more likely to provide a direct and factual answer like:

```
The capital of France is Paris.
```

The training process for instruction-tuned LLMs typically begins with a base LLM, which has been pre-trained on vast amounts of text data. This base model is then further fine-tuned using input-output pairs that consist of instructions and the model's attempts to follow those instructions. Often, this refinement process includes **Reinforcement Learning from Human Feedback (RLHF)** to enhance the system's ability to be helpful and follow instructions effectively.

One significant advantage of instruction-tuned LLMs is that they have been specifically trained to be helpful, truthful, and non-harmful. They are less prone to generating problematic or toxic outputs compared to base LLMs. As a result, many practical applications and scenarios have shifted toward the use of instruction-tuned LLMs. While some best practices available on the internet may be more tailored for base LLMs, for most real-world applications today, we recommend that most users focus on instruction-tuned LLMs. They are easier to work with and, thanks to ongoing efforts by organizations like OpenAI and other LLM companies, they are becoming safer and more aligned with ethical guidelines and user needs.

*When you're using an instruction-tuned LLM, it's a bit like giving directions to someone who's smart but doesn't know all the details of your job. Sometimes, if the LLM isn't giving you the results you want, it could be because the instructions you provided weren't clear enough.*

*For instance, if you ask it to write something about Alan Turing, it's a good idea to specify what aspect of Alan Turing you want to focus on. Do you want information about his scientific work, his personal life, his historical importance, or something else? Also, it helps to tell the LLM what style or tone you want the text to have. Should it sound like a professional journalist's article, or should it be more like a casual message to a friend? Being clear about these things helps the LLM understand what you're looking for.*

*Imagine if you were assigning this task to a recent college graduate. If you can even tell them which parts of text to read before writing about Alan Turing, it sets them up for success in completing the task the way you want it.*

**Readings/Sources:**

- [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

## What is Prompt Engineering?

<img src="https://drive.google.com/uc?export=view&id=1W5b76VkILNgJnyD1UbudJDhdsnj4YtKm" alt="PW Skills Tech">

Let's talk about "prompt engineering." This is where you provide a specific input in a certain format called a "prompt" to large language or image models. These models are really big and have been trained on massive amounts of data, including text and images.

When you give them a prompt, they use that input to generate some kind of output, which can be text, images, videos, or audio. Let's take an example: Imagine you've read a lot of books about cats. If I ask you what cats like to eat, your answer would come from all that knowledge you gained from those books. The question "What does a cat like in Winter?" provides context, and your answer would consider that context.

Similarly, when you give a prompt to these big models, the way you phrase the prompt matters a lot. If you're creative with your prompts, you can get some really interesting and informative outputs. For example, you could ask the model to explain "machine learning" to a five-year-old, and it would try to give you an answer that a five-year-old can understand. These models are super powerful and can generate all sorts of content, often beyond what you can even imagine.

So, the key takeaway here is that prompt engineering is a powerful technique for getting the kind of output you want from these large models, and the creativity you put into your prompts can lead to amazing results.

> ***Prompt Engineering is a technique used in natural language processing and with large language models (LLMs) like GPT (Generative Pre-trained Transformer) models that involves crafting clear, context-rich, and well-structured prompts to guide large language models in generating specific and useful responses. It allows users to harness the power of these models effectively for various tasks, from summarization to creative writing, by giving them the right instructions and context.***

Here's an explanation of prompt engineering:

1. **Using Clear Instructions:** When interacting with a large language model, you provide it with a prompt, which is essentially a question or statement that serves as your input. Prompt engineering involves crafting these prompts carefully to get the model to generate the type of response you want.

2. **Context and Clarity:** A well-engineered prompt provides clear context and instructions. For example, if you want the model to summarize a news article, your prompt might be something like, "Please summarize the following news article about climate change." This instructs the model to focus on summarization and on the topic of climate change.

3. **Formatting and Detail:** The way you phrase your prompt matters. You can include specific details and structure your question in a way that guides the model. For instance, if you're interested in getting a concise answer, you can frame your prompt as a question like, "What are the main causes of global warming?"

4. **Playing with Creativity:** Prompt engineering can also involve creativity. You can experiment with different phrasings and approaches to see how the model responds. For example, you could ask the model to write a story in the style of a famous author, or you could request it to explain complex concepts in simple terms.

5. **Iterative Process:** Often, prompt engineering is an iterative process. You may need to adjust and refine your prompts based on the model's initial responses until you achieve the desired output.

6. **Consider Ethical and Safety Guidelines:** It's important to use prompt engineering responsibly. Avoid prompts that could lead to harmful or biased responses. Organizations like OpenAI have guidelines and safety measures in place to ensure the responsible use of their models.

### Examples of Prompts

The few examples below illustrate how you can use well-crafted prompts to perform different types of tasks.

Topics:

- Text Summarization
- Information Extraction
- Question Answering
- Text Classification
- Conversation
- Code Generation
- Reasoning

Let's take a look at a specific example.

Imagine you're instructing a language model like GPT. You provide a prompt like:

```
Act as a product review sentiment classifier.
```

Then, you give it a review,

```
I love this product.
```

Your task is to get the model to determine whether this review is `positive` or `negative`.

If the review is `positive`, the model will generate an output to that effect. You can be creative with your prompts, asking the model to act as an AI assistant for different domains like finance or retail and request explanations.

For instance, you could provide another review:

```
Waste of money.
```

In response, the model will likely classify this as a `negative` review.

Similarly, if you input:

```
I recommend not to buy this product.
```

the model will again classify it as a negative review.

The key is that by adjusting your prompts and input, you can get the language model to perform different tasks, such as sentiment analysis on product reviews. This flexibility in prompting allows you to interact with the model and receive relevant responses.

**Readings/Sources:**

- [Examples of Prompts](https://www.promptingguide.ai/introduction/examples)

- [What is Generative AI And Prompt Engineering By Krish Naik - PW Skills Tech](https://www.youtube.com/watch?v=n7b9cbkj0_I)

## Why Prompt Engineering?

Prompt engineering is essential for several reasons:

1. **Specify Desired Output:** Language models like GPT-3 or GPT-4 are incredibly powerful, but they require clear instructions. Prompt engineering allows you to specify the type of output you want, whether it's a summary, answer to a question, creative content, or sentiment analysis. Without well-crafted prompts, these models might generate generic or undesired responses.

2. **Contextual Guidance:** Prompts provide context to the model. By crafting prompts with specific details and context, you can guide the model's responses. For example, you can ask it to summarize a news article or write a story in a particular style, and the model will follow those instructions.

3. **Adapt to Different Tasks:** Prompt engineering enables you to use the same language model for various tasks. You can adjust your prompts to make the model perform different functions, from text generation to data analysis. This versatility is valuable for users with diverse needs.

4. **Improve Relevance:** Well-constructed prompts help in getting relevant and accurate responses. If you want the model to generate information about a specific topic, a clear and relevant prompt will yield more focused and precise results.

5. **Mitigate Biases and Inappropriate Content:** Carefully crafted prompts can help mitigate biases and prevent the model from generating inappropriate or harmful content. By specifying guidelines and ethical boundaries in your prompts, you can ensure responsible AI use.

6. **Enhance User Experience:** For users interacting with language models, prompt engineering can significantly improve the overall user experience. Clear prompts lead to quicker and more accurate responses, making interactions more efficient and satisfying.

7. **Customization for Specific Domains:** If you're using language models for specialized domains like medicine or law, prompt engineering allows you to adapt the model to those fields. You can create prompts tailored to your domain's language and terminology.

8. **Responsible AI Usage:** Prompt engineering can help ensure that language models adhere to ethical guidelines and produce safe and helpful content. This is crucial for avoiding harmful outputs or unintended consequences.