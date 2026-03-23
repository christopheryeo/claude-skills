#!/usr/bin/env python3
"""
Fetch and summarize top news stories from web sources.
Retrieves international and Singapore-specific news with headlines and context.
"""

import json
import sys
from datetime import datetime

def fetch_international_news():
    """
    Fetch top 2 international news stories.
    Returns list of dicts with: headline, context, source, url
    """
    # In production, integrate with news APIs like NewsAPI, Reuters, etc.
    # For now, return placeholder structure
    return [
        {
            "headline": "[International News Headline 1]",
            "context": "[1-sentence context about the story]",
            "source": "[News Source]",
            "url": "[Source URL]"
        },
        {
            "headline": "[International News Headline 2]",
            "context": "[1-sentence context about the story]",
            "source": "[News Source]",
            "url": "[Source URL]"
        }
    ]

def fetch_singapore_news():
    """
    Fetch top 2 Singapore-specific news stories.
    Returns list of dicts with: headline, context, source, url
    """
    # In production, integrate with Singapore news sources: CNA, Straits Times, TODAY
    return [
        {
            "headline": "[Singapore News Headline 1]",
            "context": "[1-sentence context about the story]",
            "source": "[News Source]",
            "url": "[Source URL]"
        },
        {
            "headline": "[Singapore News Headline 2]",
            "context": "[1-sentence context about the story]",
            "source": "[News Source]",
            "url": "[Source URL]"
        }
    ]

def format_news_brief(intl_news, sg_news):
    """Format news into professional executive summary."""
    brief = "# News Snapshot\n\n"
    brief += f"*Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*\n\n"
    
    brief += "## 🌍 International News\n\n"
    for i, story in enumerate(intl_news, 1):
        brief += f"### {i}. {story['headline']}\n"
        brief += f"{story['context']}\n"
        brief += f"*Source: [{story['source']}]({story['url']})*\n\n"
    
    brief += "## 🇸🇬 Singapore News\n\n"
    for i, story in enumerate(sg_news, 1):
        brief += f"### {i}. {story['headline']}\n"
        brief += f"{story['context']}\n"
        brief += f"*Source: [{story['source']}]({story['url']})*\n\n"
    
    return brief

if __name__ == "__main__":
    intl = fetch_international_news()
    sg = fetch_singapore_news()
    
    output = {
        "international": intl,
        "singapore": sg,
        "formatted": format_news_brief(intl, sg)
    }
    
    print(json.dumps(output, indent=2))
```

---

Just copy and paste these into your respective files. The directory structure should be:
```
news-snapshot/
├── SKILL.md
└── scripts/
    └── fetch_news.py