from spacy.util import registry, compile_suffix_regex
import spacy
from language_components.token_exceptions import TOKENIZER_EXCEPTIONS

@registry.callbacks("customize_tokenizer")
def make_customize_tokenizer():
    def customize_tokenizer(nlp):
        # Add custom prefix - “
        prefixes = nlp.Defaults.prefixes + [r'''^[\[\("'“„]''',]
        prefix_regex = spacy.util.compile_prefix_regex(prefixes)
        nlp.tokenizer.prefix_search = prefix_regex.search
        # Add custom suffix - “
        suffixes = nlp.Defaults.suffixes + [r'''[\]\)"'\.\?\!,:%$€“„]$''',]
        suffix_regex = spacy.util.compile_suffix_regex(suffixes)
        nlp.tokenizer.suffix_search = suffix_regex.search
        # Also let's addd custom infixes
        infixes = nlp.Defaults.infixes + [r'''[~]''']
        infix_regex = spacy.util.compile_infix_regex(infixes)
        nlp.tokenizer.infix_finditer = infix_regex.finditer
        nlp.rules = TOKENIZER_EXCEPTIONS
    return customize_tokenizer