# Radiation Project
[In collaboration with Adil Rahman (Team name: CaffeineJunkieXL, 1st prize in Regional round of NASA Space Apps Challenge, 2018)]

Earth’s magnetosphere shields us from most of the cosmic radiations and the solar energetic particles that are constantly irradiated on the Earth from the Sun as well as other sources. However, this shielding effect is absent near the magnetic poles, which results in a lot of harmful radiation infiltrating to the higher altitudes in the atmosphere. Thus, polar or near-polar flights are exposed to this radiation, which may pose serious health issues for pilots, flight crew, and other frequent fliers.

## Objective
* Finding the energy flux at the location of the flight
* Computing the effective dose rate for the human, according to our normalized scale
* Computing best flight trajectory for minimum exposure to radiation between any two map locations

## Methodology
Taking into consideration the absorption of particle energy by the atmosphere, and obtaining the reduced energies of particles to get the absorption of energy by various tissues in the human body. <br>

Computing the trajectory of a flight between endpoints and displaying flight path, computation results (effective dose rate and normalized dose vs time plot). <br>

Equations provided for various calculations such as field line, loss cone angle, stopping power, stopping energy, etc. <br>

The highest and lowest values of energy flux at the location of the flight were estimated by considering extreme polar and equatorial regions, at sea level. This was used to normalize the effective dose to a 0-1 scale that was more comprehensible in layman terms.

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 6.2.1.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

## References
* Mertens, Christopher J., et al. "Geomagnetic influence on aircraft radiation exposure during a solar energetic particle event in October 2003." Space Weather 8.3 (2010): 1-16.
* NIST Physics data: https://physics.nist.gov/PhysRefData/Star/Text/ESTAR.html
* NOAA GOES electron flux: https://www.swpc.noaa.gov/products/goes-electron-flux
