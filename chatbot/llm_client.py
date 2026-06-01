import os
import time
 
os.environ["TOKENIZERS_PARALLELISM"] = "false"
 
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "Qwen/Qwen2.5-1.5B-Instruct"
 
_device = "cuda" if torch.cuda.is_available() else "cpu"
 
print(f"[LLM] Dispositivo detectado: {_device.upper()}")
print(f"[LLM] Carregando {MODEL_ID}...")
print("[LLM] (primeira execução faz download do modelo — aguarde)")
 
_tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
 
if _device == "cuda":
    _model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype=torch.float16,
        device_map="auto",
        low_cpu_mem_usage=True,
    )
else:
    _model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype=torch.float32,
        low_cpu_mem_usage=True,
    )
 
_model.eval()
print("[LLM] Modelo pronto!")
 
_SYSTEM_PROMPT = """\
Você é o "F1 Bot", um especialista apaixonado em Fórmula 1.
Responda SEMPRE em português brasileiro, de forma amigável e precisa.
Seja conciso: no máximo 10 parágrafos por resposta.
Use os dados históricos abaixo para embasar análises e previsões.
Nunca invente dados — se não souber, diga claramente.
 
{data_context}"""
 
 
def query_llm(
    user_message: str,
    data_context: str = "",
) -> tuple[str, bool]:
    """
    Gera uma resposta local com o modelo CausalLM.
 
    Parâmetros:
        user_message — pergunta/mensagem atual do usuário.
        data_context — resumo estatístico dos dados históricos de corridas.
 
    Retorna:
        (texto_da_resposta, sucesso: bool)
    """
    try:
        system_content = _SYSTEM_PROMPT.format(data_context=data_context)
 
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user",   "content": user_message},
        ]
 
        prompt_text = _tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )
 
        inputs = _tokenizer(
            prompt_text,
            return_tensors="pt",
            truncation=True,
            max_length=2048,
        ).to(_device)
 
        prompt_len = inputs["input_ids"].shape[1]
 
        start = time.time()
        with torch.no_grad():
            outputs = _model.generate(
                **inputs,
                max_new_tokens=300,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                repetition_penalty=1.15,
                pad_token_id=_tokenizer.eos_token_id,
            )
        elapsed = time.time() - start
 
        new_tokens = outputs[0][prompt_len:]
        response = _tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
 
        print(f"[LLM] Respondeu em {elapsed:.1f}s ({len(new_tokens)} tokens)")
        return response, True
 
    except Exception as e:
        print(f"[LLM] Erro na geração: {e}")
        return _fallback_response(), False
 
 
def _fallback_response() -> str:
    return (
        "Não consegui gerar uma resposta agora. "
        "Tente perguntar sobre DRS, pit stop, pilotos ou equipes da F1!"
    )
 
 
def check_connection() -> bool:
    """Sempre True — modelo local não depende de rede após o download inicial."""
    return True
 