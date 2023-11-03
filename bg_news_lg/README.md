<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Part-of-speech Tagging & Dependency Parsing (Universal Dependencies)

This project lets you train a part-of-speech tagger, morphologizer, lemmatizer and dependency parser from a [Universal Dependencies](https://universaldependencies.org/) corpus. It takes care of downloading the treebank, converting it to spaCy's format and training and evaluating the model. The template uses the [`UD_Bulgarian-BTB`](https://github.com/UniversalDependencies/UD_Bulgarian-BTB) treebank by default, but you can swap it out for any other available treebank. 


### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Convert the data to spaCy's format |
| `train` | Train UD_Bulgarian-BTB |
| `evaluate` | Evaluate on the test data and save the metrics |
| `package` | Package the trained model so it can be installed |
| `clean` | Remove intermediate files |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `train` &rarr; `evaluate` &rarr; `package` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/UD_Bulgarian-BTB` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
