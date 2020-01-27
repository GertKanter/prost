#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''

Separate the domains according to their first IPC appearance.
All domains are in the directory 'benchmarks/'.

Domain are defined by their instances. Each instance object
contains the domain file, the problem file, the directory,
and the min- and max-scores.

Domains are listed alphabetically. IPC tracks are listed
chronologically.

(Note that some domains used in the IPC 2014 are originally
from the IPC 2011.)

'''

import os

class Benchmark(object):
    def __init__(self, domain, problem, domain_path=None, horizon=40, min_score=None, max_score=None):
        self.domain = domain
        self.problem = problem
        self.path = domain_path
        self.horizon = horizon
        self.min_score = min_score
        self.max_score = max_score

    def get_domain_path(self):
        return os.getcwd() + "/benchmarks/{}/{}".format(self.path, self.domain)

    def get_problem_path(self):
        return os.getcwd() + "/benchmarks/{}/{}".format(self.path, self.problem)


ACADEMIC_ADVISING_2014 = [
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__1.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__2.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__3.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__4.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__5.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__6.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__7.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__8.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__9.rddl', 'academic-advising-2014', 40, -200.0, None),
    Benchmark('academic_advising_mdp.rddl', 'academic_advising_inst_mdp__10.rddl', 'academic-advising-2014', 40, -200.0, None),
]

ACADEMIC_ADVISING_2018 = [
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__01.rddl', 'academic-advising-2018', 20, -98.2, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__02.rddl', 'academic-advising-2018', 20, -89.5333333333, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__03.rddl', 'academic-advising-2018', 20, -100, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__04.rddl', 'academic-advising-2018', 20, -100, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__05.rddl', 'academic-advising-2018', 20, -100, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__06.rddl', 'academic-advising-2018', 30, -150, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__07.rddl', 'academic-advising-2018', 30, -150, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__08.rddl', 'academic-advising-2018', 30, -150, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__09.rddl', 'academic-advising-2018', 30, -150, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__10.rddl', 'academic-advising-2018', 30, -150, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__11.rddl', 'academic-advising-2018', 40, -200, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__12.rddl', 'academic-advising-2018', 40, -200, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__13.rddl', 'academic-advising-2018', 40, -200, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__14.rddl', 'academic-advising-2018', 40, -200, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__15.rddl', 'academic-advising-2018', 40, -200, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__16.rddl', 'academic-advising-2018', 50, -250, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__17.rddl', 'academic-advising-2018', 50, -250, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__18.rddl', 'academic-advising-2018', 50, -250, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__19.rddl', 'academic-advising-2018', 50, -250, None),
    Benchmark('academic-advising_mdp.rddl', 'academic-advising_inst_mdp__20.rddl', 'academic-advising-2018', 50, -250, None),
]

CHROMATIC_DICE_2018 = [
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__01.rddl', 'chromatic-dice-2018', 26, 14.7066666667, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__02.rddl', 'chromatic-dice-2018', 42, 40.4933333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__03.rddl', 'chromatic-dice-2018', 46, 43.7733333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__04.rddl', 'chromatic-dice-2018', 58, 45.2666666667, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__05.rddl', 'chromatic-dice-2018', 34, 46.3333333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__06.rddl', 'chromatic-dice-2018', 66, 83.2533333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__07.rddl', 'chromatic-dice-2018', 82, 111.12, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__08.rddl', 'chromatic-dice-2018', 38, 34.1866666667, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__09.rddl', 'chromatic-dice-2018', 70, 67.8933333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__10.rddl', 'chromatic-dice-2018', 86, 80.9066666667, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__11.rddl', 'chromatic-dice-2018', 42, 34.3733333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__12.rddl', 'chromatic-dice-2018', 90, 75.2533333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__13.rddl', 'chromatic-dice-2018', 46, 34.0666666667, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__14.rddl', 'chromatic-dice-2018', 66, 40.3733333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__15.rddl', 'chromatic-dice-2018', 98, 70.3333333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__16.rddl', 'chromatic-dice-2018', 98, 173.653333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__17.rddl', 'chromatic-dice-2018', 98, 243.146666667, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__18.rddl', 'chromatic-dice-2018', 98, 130.253333333, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__19.rddl', 'chromatic-dice-2018', 98, 134.52, None),
    Benchmark('chromatic-dice_mdp.rddl', 'chromatic-dice_inst_mdp__20.rddl', 'chromatic-dice-2018', 98, 136.653333333, None),
]

CROSSING_TRAFFIC_2011 = [
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__1.rddl', 'crossing-traffic-2011', 40, -32.73, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__2.rddl', 'crossing-traffic-2011', 40, -34.27, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__3.rddl', 'crossing-traffic-2011', 40, -39.03, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__4.rddl', 'crossing-traffic-2011', 40, -40.0, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__5.rddl', 'crossing-traffic-2011', 40, -38.97, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__6.rddl', 'crossing-traffic-2011', 40, -40.0, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__7.rddl', 'crossing-traffic-2011', 40, -39.47, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__8.rddl', 'crossing-traffic-2011', 40, -40.0, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__9.rddl', 'crossing-traffic-2011', 40, -39.17, None),
    Benchmark('crossing_traffic_mdp.rddl', 'crossing_traffic_inst_mdp__10.rddl', 'crossing-traffic-2011', 40, -40.0, None),
]


COOPERATIVE_RECON_2018 = [
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__01.rddl', 'cooperative-recon-2018', 30, 0.179066666667, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__02.rddl', 'cooperative-recon-2018', 30, 0.310533333333, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__03.rddl', 'cooperative-recon-2018', 30, 0.0904, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__04.rddl', 'cooperative-recon-2018', 30, 0.5424, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__05.rddl', 'cooperative-recon-2018', 40, 0.187466666667, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__06.rddl', 'cooperative-recon-2018', 40, 0.064, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__07.rddl', 'cooperative-recon-2018', 40, 0.330533333333, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__08.rddl', 'cooperative-recon-2018', 50, 0.0, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__09.rddl', 'cooperative-recon-2018', 50, 0.0, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__10.rddl', 'cooperative-recon-2018', 50, 0.502933333333, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__11.rddl', 'cooperative-recon-2018', 60, 0.0864, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__12.rddl', 'cooperative-recon-2018', 60, 0.0, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__13.rddl', 'cooperative-recon-2018', 60, 0.154133333333, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__14.rddl', 'cooperative-recon-2018', 70, 0.128933333333, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__15.rddl', 'cooperative-recon-2018', 70, 0.0, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__16.rddl', 'cooperative-recon-2018', 70, 0.0113333333333, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__17.rddl', 'cooperative-recon-2018', 80, 0.139733333333, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__18.rddl', 'cooperative-recon-2018', 80, 0.0, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__19.rddl', 'cooperative-recon-2018', 80, 0.0, None),
    Benchmark('cooperative-recon_mdp.rddl', 'cooperative-recon_inst_mdp__20.rddl', 'cooperative-recon-2018', 80, 0.0, None),
]

EARTH_OBSERVATION_2018 = [
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__01.rddl', 'earth-observation-2018', 32, -46.0533333333, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__02.rddl', 'earth-observation-2018', 40, -834.24, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__03.rddl', 'earth-observation-2018', 48, -1048.32, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__04.rddl', 'earth-observation-2018', 64, -2107.33333333, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__05.rddl', 'earth-observation-2018', 80, -1246.04, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__06.rddl', 'earth-observation-2018', 32, -402.013333333, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__07.rddl', 'earth-observation-2018', 40 -137.12, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__08.rddl', 'earth-observation-2018', 48, -629.106666667, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__09.rddl', 'earth-observation-2018', 64, -1751.53333333, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__10.rddl', 'earth-observation-2018', 80, -4145.85333333, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__11.rddl', 'earth-observation-2018', 48, -1152.6, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__12.rddl', 'earth-observation-2018', 64, -2394.82666667, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__13.rddl', 'earth-observation-2018', 80, -2473.06666667, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__14.rddl', 'earth-observation-2018', 96, -11515.16, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__15.rddl', 'earth-observation-2018', 112, -3343.22666667, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__16.rddl', 'earth-observation-2018', 48, -621.04, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__17.rddl', 'earth-observation-2018', 64 -2199.96, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__18.rddl', 'earth-observation-2018', 80, -3611.38666667, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__19.rddl', 'earth-observation-2018', 96, -5621.30666667, None),
    Benchmark('earth-observation_mdp.rddl', 'earth-observation_inst_mdp__20.rddl', 'earth-observation-2018', 112, -14684.8, None),
]

ELEVATORS_2011 = [
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__1.rddl', 'elevators-2011', 40, -65.2, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__2.rddl', 'elevators-2011', 40, -54.7, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__3.rddl', 'elevators-2011', 40, -71.7, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__4.rddl', 'elevators-2011', 40, -94.07, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__5.rddl', 'elevators-2011', 40, -111.8, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__6.rddl', 'elevators-2011', 40, -118.67, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__7.rddl', 'elevators-2011', 40, -129.63, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__8.rddl', 'elevators-2011', 40, -146.9, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__9.rddl', 'elevators-2011', 40, -160.37, None),
    Benchmark('elevators_mdp.rddl', 'elevators_inst_mdp__10.rddl', 'elevators-2011', 40, -109.7, None),
]

GAME_OF_LIFE_2011 = [
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__1.rddl', 'game-of-life-2011', 40, 70.53, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__2.rddl', 'game-of-life-2011', 40, 73.27, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__3.rddl', 'game-of-life-2011', 40, 107.17, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__4.rddl', 'game-of-life-2011', 40, 167.23, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__5.rddl', 'game-of-life-2011', 40, 203.07, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__6.rddl', 'game-of-life-2011', 40, 224.17, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__7.rddl', 'game-of-life-2011', 40, 264.97, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__8.rddl', 'game-of-life-2011', 40, 295.23, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__9.rddl', 'game-of-life-2011', 40, 311.47, None),
    Benchmark('game_of_life_mdp.rddl', 'game_of_life_inst_mdp__10.rddl', 'game-of-life-2011', 40, 176.73, None),
]


MANUFACTURER_2018 = [
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__01.rddl', 'manufacturer-2018', 30, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__02.rddl', 'manufacturer-2018', 40, 120.510933333, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__03.rddl', 'manufacturer-2018', 40, 178.050686667, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__04.rddl', 'manufacturer-2018', 40, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__05.rddl', 'manufacturer-2018', 40, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__06.rddl', 'manufacturer-2018', 40, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__07.rddl', 'manufacturer-2018', 40, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__08.rddl', 'manufacturer-2018', 40, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__09.rddl', 'manufacturer-2018', 40, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__10.rddl', 'manufacturer-2018', 50, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__11.rddl', 'manufacturer-2018', 50, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__12.rddl', 'manufacturer-2018', 50, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__13.rddl', 'manufacturer-2018', 50, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__14.rddl', 'manufacturer-2018', 60, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__15.rddl', 'manufacturer-2018', 60, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__16.rddl', 'manufacturer-2018', 70, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__17.rddl', 'manufacturer-2018', 70, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__18.rddl', 'manufacturer-2018', 80, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__19.rddl', 'manufacturer-2018', 80, 0.0, None),
    Benchmark('manufacturer_mdp.rddl', 'manufacturer_inst_mdp__20.rddl', 'manufacturer-2018', 80, 0.0, None),
]

NAVIGATION_2011 = [
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__1.rddl', 'navigation-2011', 40, -37.27, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__2.rddl', 'navigation-2011', 40, -40.0, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__3.rddl', 'navigation-2011', 40, -40.0, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__4.rddl', 'navigation-2011', 40, -39.83, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__5.rddl', 'navigation-2011', 40, -40.0, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__6.rddl', 'navigation-2011', 40, -40.0, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__7.rddl', 'navigation-2011', 40, -40.0, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__8.rddl', 'navigation-2011', 40, -38.73, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__9.rddl', 'navigation-2011', 40, -40.0, None),
    Benchmark('navigation_mdp.rddl', 'navigation_inst_mdp__10.rddl', 'navigation-2011', 40, -40.0, None),
]


PUSH_YOUR_LUCK_2018 = [
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__01.rddl', 'push-your-luck-2018', 80, 31.1466666667, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__02.rddl', 'push-your-luck-2018', 80, 37.5466666667, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__03.rddl', 'push-your-luck-2018', 80, 48.5333333333, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__04.rddl', 'push-your-luck-2018', 80, 21.6016666667, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__05.rddl', 'push-your-luck-2018', 80, 21.300234375, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__06.rddl', 'push-your-luck-2018', 80, 175.707434896, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__07.rddl', 'push-your-luck-2018', 80, 17.4816666667, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__08.rddl', 'push-your-luck-2018', 80, 27.7428255208, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__09.rddl', 'push-your-luck-2018', 80, 2162.97210124, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__10.rddl', 'push-your-luck-2018', 80, 10.1816666667, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__11.rddl', 'push-your-luck-2018', 80, 13.45796875, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__12.rddl', 'push-your-luck-2018', 80, 1599.48311483, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__13.rddl', 'push-your-luck-2018', 80, 8.67, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__14.rddl', 'push-your-luck-2018', 80, 11.2679557292, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__15.rddl', 'push-your-luck-2018', 80, 77.8681770833, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__16.rddl', 'push-your-luck-2018', 80, 50.9986979167, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__17.rddl', 'push-your-luck-2018', 80, 11.5055013021, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__18.rddl', 'push-your-luck-2018', 80, 6.939375, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__19.rddl', 'push-your-luck-2018', 80, 2.03479166667, None),
    Benchmark('push-your-luck_mdp.rddl', 'push-your-luck_inst_mdp__20.rddl', 'push-your-luck-2018', 80, 2.19208333333, None),
]

RECON_2011 = [
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__1.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__2.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__3.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__4.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__5.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__6.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__7.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__8.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__9.rddl', 'recon-2011', 40, 0.0, None),
    Benchmark('recon_mdp.rddl', 'recon_inst_mdp__10.rddl', 'recon-2011', 40, 0.0, None),
]

RED_FINNED_BLUE_EYES_2018 = [
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__01.rddl', 'red-finned-blue-eyes-2018', 60, -3233.33333, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__02.rddl', 'red-finned-blue-eyes-2018', 60, 542.8, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__03.rddl', 'red-finned-blue-eyes-2018', 60, -6624.4, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__04.rddl', 'red-finned-blue-eyes-2018', 60, -5152.0, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__05.rddl', 'red-finned-blue-eyes-2018', 60, -4486.26666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__06.rddl', 'red-finned-blue-eyes-2018', 80, -9000.66666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__07.rddl', 'red-finned-blue-eyes-2018', 80, 11796.1333333, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__08.rddl', 'red-finned-blue-eyes-2018', 80, -7258.8, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__09.rddl', 'red-finned-blue-eyes-2018', 80, -7496.13333333, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__10.rddl', 'red-finned-blue-eyes-2018', 80, 3910.93333333, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__11.rddl', 'red-finned-blue-eyes-2018', 100, -481.866666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__12.rddl', 'red-finned-blue-eyes-2018', 100, 1886.0, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__13.rddl', 'red-finned-blue-eyes-2018', 100, -6857.86666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__14.rddl', 'red-finned-blue-eyes-2018', 100, 4011.86666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__15.rddl', 'red-finned-blue-eyes-2018', 100, -8514.66666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__16.rddl', 'red-finned-blue-eyes-2018', 120, 18367.6, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__17.rddl', 'red-finned-blue-eyes-2018', 120, 8665.6, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__18.rddl', 'red-finned-blue-eyes-2018', 120, -11896.6666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__19.rddl', 'red-finned-blue-eyes-2018', 120, -6029.46666667, None),
    Benchmark('red-finned-blue-eyes_mdp.rddl', 'red-finned-blue-eyes_inst_mdp__20.rddl', 'red-finned-blue-eyes-2018', 120, -1241.86666667, None),
]

SKILL_TEACHING_2011 = [
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__1.rddl', 'skill-teaching-2011', 40, 39.34, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__2.rddl', 'skill-teaching-2011', 40, 33.75, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__3.rddl', 'skill-teaching-2011', 40, -83.23, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__4.rddl', 'skill-teaching-2011', 40, -108.73, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__5.rddl', 'skill-teaching-2011', 40, -285.95, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__6.rddl', 'skill-teaching-2011', 40, -302.99, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__7.rddl', 'skill-teaching-2011', 40, -382.86, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__8.rddl', 'skill-teaching-2011', 40, -534.7, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__9.rddl', 'skill-teaching-2011', 40, -540.62, None),
    Benchmark('skill_teaching_mdp.rddl', 'skill_teaching_inst_mdp__10.rddl', 'skill-teaching-2011', 40, -632.0, None),
]

SYSADMIN_2011 = [
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__1.rddl', 'sysadmin-2011', 40, 210.18, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__2.rddl', 'sysadmin-2011', 40, 166.68, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__3.rddl', 'sysadmin-2011', 40, 345.4, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__4.rddl', 'sysadmin-2011', 40, 311.79, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__5.rddl', 'sysadmin-2011', 40, 443.05, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__6.rddl', 'sysadmin-2011', 40, 407.16, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__7.rddl', 'sysadmin-2011', 40, 513.74, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__8.rddl', 'sysadmin-2011', 40, 426.46, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__9.rddl', 'sysadmin-2011', 40, 612.06, None),
    Benchmark('sysadmin_mdp.rddl', 'sysadmin_inst_mdp__10.rddl', 'sysadmin-2011', 40, 471.1, None),
]

TAMARISK_2014 = [
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__1.rddl', 'tamarisk-2014', 40, -633.01, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__2.rddl', 'tamarisk-2014', 40, -948.98, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__3.rddl', 'tamarisk-2014', 40, -820.54, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__4.rddl', 'tamarisk-2014', 40, -1178.76, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__5.rddl', 'tamarisk-2014', 40, -1276.74, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__6.rddl', 'tamarisk-2014', 40, -1432.27, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__7.rddl', 'tamarisk-2014', 40, -1452.65, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__8.rddl', 'tamarisk-2014', 40, -1629.29, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__9.rddl', 'tamarisk-2014', 40, -1463.72, None),
    Benchmark('tamarisk_mdp.rddl', 'tamarisk_inst_mdp__10.rddl', 'tamarisk-2014', 40, -1758.88, None),
]

TRAFFIC_2011 = [
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__1.rddl', 'traffic-2011', 40, -19.97, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__2.rddl', 'traffic-2011', 40, -47.87, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__3.rddl', 'traffic-2011', 40, -63.93, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__4.rddl', 'traffic-2011', 40, -119.33, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__5.rddl', 'traffic-2011', 40, -120.7, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__6.rddl', 'traffic-2011', 40, -156.67, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__7.rddl', 'traffic-2011', 40, -146.57, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__8.rddl', 'traffic-2011', 40, -154.37, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__9.rddl', 'traffic-2011', 40, -108.03, None),
    Benchmark('traffic_mdp.rddl', 'traffic_inst_mdp__10.rddl', 'traffic-2011', 40, -243.7, None),
]

TRIANGLE_TIREWORLD_2014 = [
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__1.rddl', 'triangle-tireworld-2014', 40, -32.27, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__2.rddl', 'triangle-tireworld-2014', 40, -28.47, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__3.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__4.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__5.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__6.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__7.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__8.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__9.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
    Benchmark('triangle_tireworld_mdp.rddl', 'triangle_tireworld_inst_mdp__10.rddl', 'triangle-tireworld-2014', 40, -40.0, None),
]

WILDFIRE_2014 = [
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__1.rddl', 'wildfire-2014', 40, -4126.83, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__2.rddl', 'wildfire-2014', 40, -14146.83, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__3.rddl', 'wildfire-2014', 40, -10424.5, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__4.rddl', 'wildfire-2014', 40, -23154.0, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__5.rddl', 'wildfire-2014', 40, -8169.83, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__6.rddl', 'wildfire-2014', 40, -24726.33, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__7.rddl', 'wildfire-2014', 40, -16646.67, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__8.rddl', 'wildfire-2014', 40, -26196.67, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__9.rddl', 'wildfire-2014', 40, -18122.5, None),
    Benchmark('wildfire_mdp.rddl', 'wildfire_inst_mdp__10.rddl', 'wildfire-2014', 40, -27999.67, None),
]

WILDLIFE_PRESERVE_2018 = [
    Benchmark('wildlife-preserve_01_mdp.rddl', 'wildlife-preserve_inst_mdp__01.rddl', 'wildlife-preserve-2018', 60, 861.6948, None),
    Benchmark('wildlife-preserve_02_mdp.rddl', 'wildlife-preserve_inst_mdp__02.rddl', 'wildlife-preserve-2018', 60, 772.2744, None),
    Benchmark('wildlife-preserve_03_mdp.rddl', 'wildlife-preserve_inst_mdp__03.rddl', 'wildlife-preserve-2018', 60, 784.024133333, None),
    Benchmark('wildlife-preserve_04_mdp.rddl', 'wildlife-preserve_inst_mdp__04.rddl', 'wildlife-preserve-2018', 60, 661.932, None),
    Benchmark('wildlife-preserve_05_mdp.rddl', 'wildlife-preserve_inst_mdp__05.rddl', 'wildlife-preserve-2018', 60, 537.096, None),
    Benchmark('wildlife-preserve_06_mdp.rddl', 'wildlife-preserve_inst_mdp__06.rddl', 'wildlife-preserve-2018', 60, 701.793866667, None),
    Benchmark('wildlife-preserve_07_mdp.rddl', 'wildlife-preserve_inst_mdp__07.rddl', 'wildlife-preserve-2018', 60, 268.610666667, None),
    Benchmark('wildlife-preserve_08_mdp.rddl', 'wildlife-preserve_inst_mdp__08.rddl', 'wildlife-preserve-2018', 60, 727.618, None),
    Benchmark('wildlife-preserve_09_mdp.rddl', 'wildlife-preserve_inst_mdp__09.rddl', 'wildlife-preserve-2018', 60, 751.386666667, None),
    Benchmark('wildlife-preserve_10_mdp.rddl', 'wildlife-preserve_inst_mdp__10.rddl', 'wildlife-preserve-2018', 60, 636.292266667, None),
    Benchmark('wildlife-preserve_11_mdp.rddl', 'wildlife-preserve_inst_mdp__11.rddl', 'wildlife-preserve-2018', 60, 1049.56306667, None),
    Benchmark('wildlife-preserve_12_mdp.rddl', 'wildlife-preserve_inst_mdp__12.rddl', 'wildlife-preserve-2018', 60, 574.419066667, None),
    Benchmark('wildlife-preserve_13_mdp.rddl', 'wildlife-preserve_inst_mdp__13.rddl', 'wildlife-preserve-2018', 60, 758.8136, None),
    Benchmark('wildlife-preserve_14_mdp.rddl', 'wildlife-preserve_inst_mdp__14.rddl', 'wildlife-preserve-2018', 60, 777.9772, None),
    Benchmark('wildlife-preserve_15_mdp.rddl', 'wildlife-preserve_inst_mdp__15.rddl', 'wildlife-preserve-2018', 60, 1252.9972, None),
    Benchmark('wildlife-preserve_16_mdp.rddl', 'wildlife-preserve_inst_mdp__16.rddl', 'wildlife-preserve-2018', 60, 695.311866667, None),
    Benchmark('wildlife-preserve_17_mdp.rddl', 'wildlife-preserve_inst_mdp__17.rddl', 'wildlife-preserve-2018', 80, 1467.67613333, None),
    Benchmark('wildlife-preserve_18_mdp.rddl', 'wildlife-preserve_inst_mdp__18.rddl', 'wildlife-preserve-2018', 80, 547.9844, None),
    Benchmark('wildlife-preserve_19_mdp.rddl', 'wildlife-preserve_inst_mdp__19.rddl', 'wildlife-preserve-2018', 80, 1595.51253333, None),
    Benchmark('wildlife-preserve_20_mdp.rddl', 'wildlife-preserve_inst_mdp__20.rddl', 'wildlife-preserve-2018', 80, 769.4372, None),
]


# Domains used in the IPC 2011.
IPC2011 =  CROSSING_TRAFFIC_2011 + \
           ELEVATORS_2011 + \
           GAME_OF_LIFE_2011 + \
           NAVIGATION_2011 + \
           RECON_2011 +\
           SKILL_TEACHING_2011 + \
           SYSADMIN_2011 + \
           TRAFFIC_2011

# Domains used in the IPC 2014.
IPC2014 =  ACADEMIC_ADVISING_2014 + \
           CROSSING_TRAFFIC_2011 + \
           ELEVATORS_2011 + \
           SKILL_TEACHING_2011 + \
           TAMARISK_2014 + \
           TRAFFIC_2011 + \
           TRIANGLE_TIREWORLD_2014 + \
           WILDFIRE_2014

# Domains used in the IPC 2018.
IPC2018 = ACADEMIC_ADVISING_2018 + \
          CHROMATIC_DICE_2018 +  \
          COOPERATIVE_RECON_2018 + \
          EARTH_OBSERVATION_2018 + \
          MANUFACTURER_2018 + \
          PUSH_YOUR_LUCK_2018 + \
          RED_FINNED_BLUE_EYES_2018 + \
          WILDLIFE_PRESERVE_2018

# Domains used in some IPC, removing duplicates.
IPC_UNTIL_2014 = list(set().union(IPC2011 + IPC2014))
IPC_UNTIL_2018 = list(set().union(IPC2011 + IPC2014 + IPC2018))
IPC_ALL = list(set().union(IPC2011 + IPC2014 + IPC2018))
