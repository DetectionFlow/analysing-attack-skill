# Analysing ATT&CK Skill

## Overview

Claude skill to assist LLM-powered analysis of Mitre ATT&CK techniques and sub-techniques. Use during detection engineering, CTI analysis, threat modelling, incident response or any other cybersecurity tasks.

Equips Claude with best practice and guidance for mapping ATT&CK techniques. Includes LLM optimised, token-efficient, resource files containing up to date context on all ATT&CK v19.2 technques and sub-techniques in a format specifiaclly designed for AI agents.

## Usage

This skill can be used with Claude or any other AI agent (For ex. LangChain DeepAgents) that supports [Anthropics Skills feature](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

Download the [analysing-attack-skill.zip](analysing-attack-skill.zip) file from this repo and install following your chosen AI agents documentation.

- [Claude AI](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Claude Code](https://code.claude.com/docs/en/skills)
- [LangChain Deep Agents](https://blog.langchain.com/using-skills-with-deep-agents/)

Alternativly, simply include the individual markdown files within prompts as required.

## Detailed Information

Resource files within this skill have been processed into a format specially designed for AI deep agents (such as Claude Code) to optimse token usage and maximise context efficiency. AI deep agents are able to progressibly load in skills and use commandline tools such as grep to selectivly search for keywords or IDs.

Each ATT&CK technique has been compressed using an LLM into a single line containing ID, Name, Keywords, Description and Platform. 

Skills offer more token-efficent context and reduced tool calling latency over MCP or native tools fucntions and less complex setup and retrival than RAG. 

## Regenerating the Resources

`generate.py` builds everything in the skill folder from the official ATT&CK STIX data. Copy `.env.example` to `.env`, add your Anthropic API key, then:

```
uv run generate.py           # compress new or changed techniques, rewrite resources and zip
uv run generate.py --all     # recompress every technique
uv run generate.py --check   # verify committed files against STIX and the cache (no LLM calls)
```

Compressed rows are cached in `technique_cache.json`, keyed on a hash of each technique's source text, so only techniques that changed are sent to the model (claude-opus-5-5). Every response is validated and retried before anything is written. The technique tables, group list and stats in the changelog are generated from STIX; the rest of the changelog and `SKILL.md` are hand-written and checked for invalid technique IDs.

To move to a new ATT&CK release, bump `ATTACK_VERSION` and add the release date to `RELEASES` in `generate.py`, add a row to the Version Timeline in the changelog, then run the script.

## TODO

Additional resources will be added, such as Detection Strategies and Analytics. 

A [Evaluator-Optimiser](https://www.anthropic.com/engineering/building-effective-agents) workflow may be created to improve quality of outputs.

Develop evaluation harness to assess different compression models quality/costs and to benchmark effectiveness of Skills vs MCP/Tools/RAG.


