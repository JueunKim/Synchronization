# Synchronizing transcripts/ subtitles  
 Tools for synchronizing transcript and subtitles. The project is developed by Emory NLP lab.

### Requirement
- Install [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) package. 


### Usage
- To run the program, follow below four step.
	
  1. json_cleaning.py
		- extract all transcript, utterance_id, speaker from .json file.
		- input file -> .json file.
	 	- output file format -> pickle dumped .txt file. 

	2. smi_cleaning.py
		- extract each subtitle with start/end time(milliseconds) from .smi(subtitle) file
		- input file -> .smi(subtitle) file
		- output file format ->  pickle dumped .txt file 
   
  3. smi_superset.py
  	  	- make subtitle superset for all possible uttrance from .smi(subtitle) file. 
    	- input file -> pickle dumped .txt file (from step2)
    	- output file format -> pickle dumped .txt file.
    
	4. matching.py
		- apply fuzzywuzzy matching algorithms
		- input file ->  step1 output file(extracted transcript) && step3 output file(superset of subtitle)
    	- output file -> result of matching  



### Future work