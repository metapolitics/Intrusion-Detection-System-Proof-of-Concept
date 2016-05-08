# Intrusion-Detection-System-Proof-of-Concept

##[Please read the wiki](https://github.com/sweetmanC/Intrusion-Detection-System-Proof-of-Concept/wiki)


Within the packaged file, the following files exist:

```
/attack/
	/1-1-ffb/
	/1-1-format/
	/2-2-ipsweep/
	/2-5-ftpwrite/
	/3-1-ffb/
	/3-3-ftpwrite/
	/3-4-warez/
	/3-5-warezmaster/
	/4-1-warezclient/
	/4-2-spy/
/training/
	method1.py
	method2.py
```

The attack directory contains the ten attack profiles as provided by the course, and the training directory contains the 100 training traces that are used by the algorithms to learn normal system behaviour. Both Python script files are named in accordance with their method number. Within the Python script’s the location of the data sources are programmed relative to the Python source code and are to remain within the same folder as the scripts.
In order to run the Python scripts, the following commands will need to be executed:
```
	~/path/ $ python method1.py
	~/path/ $ python method1.py
```

