# Bulgarian spaCy core models (BGspaCy)
You can find all the models in [Huggingface](https://huggingface.co/sakelariev). This repo contains config files for:

* bg_news_sm
* bg_news_lg
* bg_news_trf

All Bulgarian pipelines contains a tokenizer, trainable lemmatizer, POS tagger, dependency parser, morphologizer and NER components. The dataset for the NER pipeline is currently shared only privately (trying to figure out how to share it publicly without any copyright issues), so if you need it just email me.

### Installation
You can download all the models from Huggingface:

Small Bulgarian model: `pip install https://huggingface.co/turkish-nlp-suite/tr_core_news_md/resolve/main/tr_core_news_md-any-py3-none-any.whl` <br>
Large Bulgarian model: `pip install https://huggingface.co/turkish-nlp-suite/tr_core_news_lg/resolve/main/tr_core_news_lg-any-py3-none-any.whl` <br>
Transformer based Bulgarian model: `pip install https://huggingface.co/turkish-nlp-suite/tr_core_news_trf/resolve/main/tr_core_news_trf-any-py3-none-any.whl`

### Usage
After installing the models via pip you can directly use by loading into spaCy:

```
import spacy
nlp = spacy.load("bg_news_sm")

doc = nlp("През 1843 г. Петко Славейков става учител в Търново.")
```

### Tutorials
Coming soon

### License
**CC-BY-NC-SA-3.0**

Sadly the original license of the [Bulgarian Treebank](https://github.com/UniversalDependencies/UD_Bulgarian-BTB), which was used for the training of the main pipeline components (pretty much everything without the NER) was released under this non-commercial/share-alike license, which prevents me to release that models under any other license terms (my intention was releasing this under the MIT license). So all of the models cannot be used for commercial purposes. 


### Future work
I'm planning to release more Bulgarian models for spaCy, so I consider this repo an ongoing project. Some of the models I have already started working on:

* bg_web_sm, bg_web_lg, bg_web_trf – improved NER models (right now the models are trained only a news text corpus for only 3 labels). Those models are going to be trained on a mixed corpus of web data – news, legal, fiction, conversation data. Also planning to add more labels - `PERSON`, `GPE`, `LOC`, `ORG`, `LANGUAGE`, `NAT_REL_POL`, `DATETIME`, `PERIOD`, `QUANTITY`, `MONEY`, `ORDINAL`, `FACILITY`, `WORK_OF_ART`, `EVENT`

* bg_news_sm, bg_news_lg, bg_news_trf 2.0 versions. Train on new data and add new labels - `PERSON`, `GPE`, `LOC`, `ORG`, `LANGUAGE`, `NAT_REL_POL`, `DATETIME`, `PERIOD`, `QUANTITY`, `MONEY`, `ORDINAL`, `FACILITY`, `WORK_OF_ART`, `EVENT`

* coreference resolution spaCy model for Bulgarian
