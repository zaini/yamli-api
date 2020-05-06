from yamliwrapper import Transliterator


def test_yamli():
    transliteration = Transliterator("salam")
    words = transliteration.candidates

    # transliteration2 = Transliterator("7aga 7aga")
    # words2 = transliteration2.candidates

    assert words[0] == "سلام", "Incorrect response from call for 'salam'. Yamli API may be down from their end."
    # assert words2[0] == "حاجة حاجة", "Incorrect response from call for '7aga 7aga'"
