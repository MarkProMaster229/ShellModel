import tkinter as tk
import threading
from dowlound import Dowlound
import importlib.util




class ShellGUI:
    def __init__(self, master):
        self.master = master
        master.title("Прототип GUI для модели")
        master.geometry("500x400")

        self.label = tk.Label(master, text="Введите данные для модели:")
        self.label.pack(pady=5)

        self.input_text = tk.Text(master, height=5, width=50)
        self.input_text.pack(pady=5)

        self.run_button = tk.Button(master, text="Запустить модель", command=self.run_model)
        self.run_button.pack(pady=10)

        self.output_label = tk.Label(master, text="Результат модели:")
        self.output_label.pack(pady=5)

        self.output_text = tk.Text(master, height=10, width=50, state='normal')
        self.output_text.pack(pady=5)


        #например моя модель 
    def modelOutput(self):
        from transformers import AutoTokenizer, AutoModelForCausalLM
        tokenizer = AutoTokenizer.from_pretrained("MarkProMaster229/InternetLanguage")
        model = AutoModelForCausalLM.from_pretrained("MarkProMaster229/InternetLanguage")
        input_text = self.input_text.get("1.0", tk.END).strip()
        inputs = tokenizer(input_text, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50, do_sample=True, top_k=50, top_p=0.95)
        print(tokenizer.decode(outputs[0], skip_special_tokens=True))
        global output
        output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return output

        
    def run_model(self):
        input_data = self.input_text.get("1.0", tk.END).strip()
        if not input_data:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Ничего не введено.")
            return
        threading.Thread(target=self.model_inference, args=(input_data,)).start()

    def model_inference(self, input_data):
        self.dowFile = Dowlound
        self.model_module = self.dowFile.uploadfileModel("run.py")

        self.output_text.after(0, lambda: self.update_output(self.modelOutput()))
        
    def update_output(self, result):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

class Finaly:
    def __init__(self):
        self.dowFile = Dowlound
        self.model_module = self.dowFile.uploadfileModel("run.py")
    # Или если модель просто класс
    # model_instance = model_module.MyModel()




if __name__ == "__main__":
    root = tk.Tk()
    gui = ShellGUI(root)
    root.mainloop()
