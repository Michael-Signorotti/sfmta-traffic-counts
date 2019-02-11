# SFMTA Traffic Counts - PDF to CSV

This repository includes a series of functions for extracting the SFMTA traffic counts (1995-2015) from a PDF file to a CSV file. The PyPDF2 and tabula Python packages
are utilized for this task.

The SFMTA traffic counts can be found at the following (link)[https://www.sfmta.com/reports/sfmta-traffic-count-data-1995-2015].

## Instructions

Create a conda environment named traffic-counts from the provided environment file with the following command.

```
conda env create -f environment.yml
```

Now, we can activate the virtual environment. If you are using Windows, delete "source" from the below command.

```
source activate traffic-counts
```

Run the script and create a csv file in your working directory named *traffic_counts.csv*.

```
python traffic_counts.py
```


## License

    Copyright 2019 Michael Signorotti

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.