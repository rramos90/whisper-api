import whisper
import tempfile

model = whisper.load_model("base")  # use "small" ou "medium" se precisar de melhor qualidade

def transcribe_and_summarize(audio_file):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as temp_audio:
        audio_file.save(temp_audio.name)
        result = model.transcribe(temp_audio.name)
        transcription = result["text"]

        resumo = gerar_resumo_consultoria(transcription)
        return {
            "transcricao": transcription,
            "relatorio": resumo
        }

def gerar_resumo_consultoria(texto):
    # Simulação simples com regras — pode ser substituído depois por LLM local
    pautas = []
    linhas = texto.split('. ')
    for i, l in enumerate(linhas[:5]):
        pautas.append(f"- Pauta {i+1}: {l.strip()}")
    
    return f"RELATÓRIO DE CONSULTORIA COMERCIAL\n\nPautas Abordadas:\n" + "\n".join(pautas)
