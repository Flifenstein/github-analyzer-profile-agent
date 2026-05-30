Timeline of building this
Day 1 - let's start with scaffholding, love the overview
- okay let's write the score_repo, easy part
- oh shoot, yes, i said this time i'll work with uv. let's install it
- okay so the LLM advised me to do look at pydantic for the data schema. cool stuff, naturally wouldn't thought about it until later
-ah yes, this repo I'd say i'd have tests in. let's write the god damn tests cases wohoo
- i realized i had snake_case mistakes (cuz I write code like I write on paper...illegibable) so i installed ruff. it has been ruff around
- always check your gitignore girl
- ah yes. i need pylance so i can hover over these functions that i forget what they do and see where they are placed


Day 2
- look onYT videos on how to organize my efolder repo, hence the insane commit of making sure all the files are in the right folders
- add some extenstions like pydantic 
-read docs out fo curiosity

Day 3
- committed cached files by mistake so did git rm -r --cached .
- finished repo score

made the mental schema of
Agent 1 produces → ProfileAnalysis   
Agent 2 produces → ResearchFindings 
Agent 4 produces → ApprovedChanges    
- locked in the amazing research findings, that one was easy
- the improvement plan, that one was harder to logically think through since i needed a new validator form the chnage of topics if there are new finidngs proposed
- co write the test with AI because there is a lot to write, i just made sure it checks all the logic of schemas
