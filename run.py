
def modelOutput():
    from transformers import AutoTokenizer, AutoModelForCausalLM
    tokenizer = AutoTokenizer.from_pretrained("MarkProMaster229/InternetLanguage")
    model = AutoModelForCausalLM.from_pretrained("MarkProMaster229/InternetLanguage")
    input_text = "Привет! Как дела?"
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50, do_sample=True, top_k=50, top_p=0.95)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
    global output
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output