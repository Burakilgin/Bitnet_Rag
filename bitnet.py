import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from prompt_temp import prompt


class BitnetLLM:
    def __init__(self):
        model_id = "microsoft/bitnet-b1.58-2B-4T"
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16
        )
        self.model.eval()

    def invoke(self, input_data: dict):
        question = input_data.get("question", "")
        context = input_data.get("documents", "")

        full_prompt = f"{prompt}\n\nContext:\n{context}\n\nUser Question:\n{question}\nAnswer:"

        inputs = self.tokenizer(full_prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=150,
                pad_token_id=self.tokenizer.eos_token_id
            )

        answer = self.tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[-1]:],
            skip_special_tokens=True
        )
        return answer