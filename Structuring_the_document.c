//This is my submission for the HackerRank Problem "Structuring the Document".
//Link : <https://www.hackerrank.com/challenges/structuring-the-document>.
//Level : Hard

struct document get_document(char* text) {
struct document doc;
    struct paragraph *cur_paragraph = NULL;
    struct sentence *cur_sentence = NULL;
    char *new_word = NULL;

    doc.data = NULL;
    doc.paragraph_count = 0;

    for (char *s = text; *s; ++s)
    {
        if (*s == ' ' || *s == '.')
        {
            
            if (cur_paragraph == NULL)
            {
                doc.paragraph_count++;
                doc.data = (struct paragraph *) realloc(doc.data, sizeof(struct paragraph) * doc.paragraph_count);

                cur_paragraph = doc.data + doc.paragraph_count - 1;
                cur_paragraph->data = NULL;
                cur_paragraph->sentence_count = 0;

                cur_sentence = NULL;
            }
            if (cur_sentence == NULL)
            {
                cur_paragraph->sentence_count++;
                cur_paragraph->data = (struct sentence *) realloc(cur_paragraph->data, sizeof(struct sentence) * cur_paragraph->sentence_count);

                cur_sentence = cur_paragraph->data + cur_paragraph->sentence_count - 1;
                cur_sentence->data = NULL;
                cur_sentence->word_count = 0;
            }

            cur_sentence->word_count++;
            cur_sentence->data = (struct word *) realloc(cur_sentence->data, sizeof(struct word) * cur_sentence->word_count);
            cur_sentence->data[cur_sentence->word_count - 1].data = new_word;
            new_word = NULL;

            if (*s == '.')
                cur_sentence = NULL;       
            *s = 0;
        }

        else if (*s == '\n')
        {
            cur_sentence = NULL;
            cur_paragraph = NULL;
        }
        else
        {
            if (new_word == NULL)
            {
                new_word = s;
            }
        }
    }

    return doc;
}

struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
return Doc.data[n - 1].data[m - 1].data[k - 1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) { 
return Doc.data[m - 1].data[k - 1];
}

struct paragraph kth_paragraph(struct document Doc, int k) {
return Doc.data[k - 1];
}

