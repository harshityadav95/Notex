"""Prepare standalone study prose while keeping archived originals and credits intact."""
import re

PUBLISHER = re.compile(r"o[’' -]?reilly|oreil\.ly|oreilly\.com|FAANG_BOOKS|Early Release|sgrey@", re.I)
DROP_SECTIONS = {
    'A Note for Early Release Readers', 'Footnotes', 'References',
    'O’Reilly Online Learning', 'How to Contact Us', 'Acknowledgments',
    'Conventions Used in This Book',
}
GUIDE = {
    'Who Should Read This Book?': ('Study goals', '''Use these notes to reason about how data systems behave under real workloads.

- Choose storage and processing approaches from requirements rather than popularity.
- Explain the trade-offs between latency, consistency, availability, and cost.
- Trace what happens when a node, network link, or dependency fails.
- Separate the authoritative data from caches, indexes, and other derived views.

A working knowledge of application development, SQL, HTTP, and basic networking is useful. The ideas apply across programming languages and frameworks.'''),
    'What’s New in the Second Edition?': ('Topics in this learning path', '''The modules move from requirements and data models to storage, replication, transactions, and processing.

| Area | Questions to answer |
| --- | --- |
| Foundations | What does the workload require? How should data be modeled and stored? |
| Distributed systems | How do replicas, shards, clocks, and consensus affect correctness? |
| Processing | When should work run in batches, and when should events flow continuously? |
| Responsibility | What should be collected, retained, shared, and deleted? |

Follow the modules in order for a connected explanation, or use the syllabus to revisit a specific topic.'''),
    'References and Further Reading': ('A practical study method', '''For each lesson, write down the mechanism, the assumptions it relies on, and the failure mode it prevents.

1. Read the explanation and sketch the data flow.
2. Walk through an ordinary request, then repeat the trace with one component unavailable.
3. Compare the approach with an alternative and identify the trade-off.
4. Keep a short example or question in your own notes.
5. Mark the lesson as understood when you can explain it without looking back.

Use the module recap to connect the individual mechanisms. Revisit any lesson whose assumptions remain unclear.'''),
}


def code(text):
    # Only illustrative repository/package paths change; executable logic is untouched.
    text = re.sub(r'github\.com/learning-go-book-3e/ch\d+/sample_code/', 'example.com/studynotes/', text)
    return text.replace('sample_code/artifact/', 'examples/artifact/')


def _plain(text, strip_citations=True):
    # Publishing and exercise-solution location sentences are not part of the lesson.
    text = re.sub(r'[^.!?\n]*(?:Solutions? (?:are |can be |to (?:these|the) exercises)|[Aa]nswers? to (?:these|the) exercises)[^.!?\n]*(?:repository|directory)[^.!?\n]*[.!?]?', '', text)
    text = re.sub(r'\s+or in the `sample_code/[^`]+` directory in the Chapter \d+ repository', '', text, flags=re.I)
    text = re.sub(r'\s+or in the `[^`]+` directory in the (?:Chapter \d+|chapter) repository', '', text, flags=re.I)
    text = re.sub(r'\s*\((?:see )?Chapter(?:s)? \d+[^)]*\)', '', text, flags=re.I)
    if strip_citations:
        text = re.sub(r' +\[(?:\d+)(?:\s*[,–-]\s*\d+)*\](?![\w(])', '', text)
    text = re.sub(r'\b(?:this|the) book\b', lambda m:'These notes' if m[0][0].isupper() else 'these notes', text, flags=re.I)
    text = re.sub(r'\b(?:this|the previous|the next) chapter\b', lambda m:'This topic' if m[0][0].isupper() else 'this topic', text, flags=re.I)
    text = re.sub(r'\bChapters? \d+(?: (?:and|or) \d+)?\b', 'the related discussion', text)
    # Remove consecutive accidental duplicate narrative sentences without touching code.
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    result = []
    for sentence in sentences:
        if not result or sentence != result[-1]:
            result.append(sentence)
    if len(result)%2==0 and result[:len(result)//2]==result[len(result)//2:]:
        result=result[:len(result)//2]
    return re.sub(r' +([,.;:])', r'\1', ' '.join(result))


def _prose(text, strip_citations=True):
    text=re.sub(r'\s+or in the [^\n]*?Chapter \d+ repository', '', text)
    text=text.replace('You can find the code for this example on GitHub. ', '').replace('You can see it on GitHub.', '')
    text=text.replace('For example, I wrote a simple Lisp interpreter with a Scan function', 'For example, a simple Lisp interpreter can use a Scan function')
    text=text.replace('If you don’t have Docker installed or if you want to build the code for yourself, you can find the math-server code on GitHub.', 'If Docker is unavailable, use a local test server that implements the same API.')
    text=re.sub(r'github\.com/learning-go-book-3e/ch\d+/`(?:sample_code|examples)/([^`]+)`',r'`example.com/studynotes/\1`',text)
    text=code(text)
    text=re.sub(r'\b(?:(?:The )?[Ss]olutions? (?:are|can be found|are available)|(?:The )?[Aa]nswers? (?:are|can be found)|You can find (?:answers|solutions)|They are found)[^.!?\n]*(?:directory|repository)[^.!?\n]*[.!?]?', '', text)
    text=re.sub(r'\s+(?:in|of|from) (?:the )?Chapter \d+ repository','',text,flags=re.I)
    text=text.replace('sample_code/', 'examples/').replace('sample_code directory','examples directory')
    text=re.sub(r'^3\. In the `exercises/ex03` directory[^\n]+', '3. Write a function `split` that accepts a string and a separator and returns the nonempty parts. Review its parameter handling, return values, and control flow, and explain how each choice improves clarity.', text)
    text=re.sub(r'\s+or in the `[^`]+` directory in the Chapter \d+ repository','',text,flags=re.I)
    text=re.sub(r'\([^)]*\bChapter(?:s)? \d+[^)]*\)','',text)
    text=re.sub(r'(?i)(?:As (?:we shall|you will|you’ll) see|as discussed|as covered) in Chapters? \d+(?: and \d+)?,?\s*','',text)
    return ''.join(piece if piece.startswith('`') else _plain(piece, strip_citations) for piece in re.split(r'(`+[^`]+`+)',text))


def clean(text, strip_citations=True):
    """Clean prose outside code fences; remove only publishing/reader interface content."""
    text = re.sub(r'\n---\s*\n\s*- table of contents\b.*', '', text, flags=re.S|re.I)
    text = text.replace('<!-- Skip to Content -->', '')
    pieces = re.split(r'(^```[^\n]*\n.*?^```[^\n]*)', text, flags=re.M|re.S)
    for i, piece in enumerate(pieces):
        if piece.startswith('```'):
            pieces[i] = code(piece)
            continue
        # Preserve structural line breaks, lists, tables, and inline code.
        lines = []
        for line in piece.splitlines():
            if PUBLISHER.search(line):
                continue
            if line.startswith('#'):
                lines.append(line)
                continue
            if line.strip() in ('- table of contents', '- search', '- settings', '- Previous chapter', '- Next chapter', '- Table of contents collapsed'):
                continue
            lines.append(_prose(line, strip_citations))
        pieces[i] = '\n'.join(lines)
        if piece.startswith('\n'): pieces[i]='\n'+pieces[i]
        if piece.endswith('\n'): pieces[i]+='\n'
    return ''.join(pieces).strip()+'\n'
