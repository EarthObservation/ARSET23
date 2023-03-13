# Practical

Materials for the *Crop Mapping using Synthetic Aperture Radar (SAR) and Optical Remote Sensing*.

Prepared by:  
Krištof Oštir  
Matej Račič 

## Installation instructions
We will be using [Anaconda](https://www.anaconda.com/), which can be installed from the [website](https://www.anaconda.com/products/distribution#Downloads).
Once installed open Anaconda Prompt and move to the location of the extracted repository `cd Downloads/ARSET23/Practical`. If you have downloaded it to a different drive type the letter of the drive first `D:`.

Here you can create a new environment for this tutorial using the provided `environment.yml` file:

```
conda env create --name eo --file environment.yml
conda activate eo
```

Alternatively, you can use pip to install the libraries using 'pip' and follow the tutorial. This will take some time. Once installed run `jupyter lab` and a browser tab will open.

## Practicals
We will be using the notebooks available in the corresponding folders. To run the notebook after the practical you will need a [Sentinel Hub](https://www.sentinel-hub.com/develop/api/ogc/standard-parameters/) account.
Free trial is also available. Once registered you can follow the [instructions](https://sentinelhub-py.readthedocs.io/en/latest/configure.html) to configure access to the services or use `sentinelhub.id` with `credentials_SH.ipynb`.

## Additional resources
This tutorial is based on the [materials](https://github.com/sentinel-hub/eo-learn-workshop/) provided by Sinergise. Where you can find even more examples and resources for the [eo-learn](https://github.com/sentinel-hub/eo-learn) library.

## Acknowledgment

Preparation of the materials was part financed by the Slovenian Research Agency core funding No. P2-0406.

## License
This project is licensed under the terms of the [Apache License](LICENSE).

© Copyright 2022 University of Ljubljana, Faculty of Civil and Geodetic Engineering
