# Analysing ATT&CK Skill

## Overview

Claude skill to assist LLM-powered analysis of Mitre ATT&CK techniques and sub-techniques. Use during detection engineering, CTI analysis, threat modelling, incident response or any other cybersecurity tasks.

Equips Claude with best practice and guidance for mapping ATT&CK techniques. Includes LLM optimised, token-efficient, resource files containing up to date context on all ATT&CK v18.1 technques and sub-techniques in a format specifiaclly designed for AI agents.

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

The included notebook can be used to generate the compressed resouce files. claude-haiku-4-5-20251001 costs approx $0.55 for all 691 techniques.

## TODO

Additional resources will be added, such as Detection Strategies and Analytics. 

A [Evaluator-Optimiser](https://www.anthropic.com/engineering/building-effective-agents) workflow may be created to improve quality of outputs.

Develop evaluation harness to assess different compression models quality/costs and to benchmark effectiveness of Skills vs MCP/Tools/RAG.


