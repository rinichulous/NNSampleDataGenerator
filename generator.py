import random

movement = {}

movement = {
    0: {
      'a1': {
        'min': -0.9374,
        'max': -0.9260
      },
      'a2': {
        'min': -0.1963,
        'max': -0.1261
      },
      'a3': {
        'min': 0.0693,
        'max': 0.2824
      },
      'a4': {
        'min': -0.0359,
        'max': 0.1113
      },
      'signalPower': 0.4821,
      'outputs': {
          0: 1.0,
          1: 0.0,
          2: 0.0,
          3: 0.0,
          4: 0.0,
          5: 0.0
      }
    },
    1: {
      'a1': {
        'min': -1.6957,
        'max': -1.4096
      },
      'a2': {
        'min': 0.0333,
        'max': 0.3154
      },
      'a3': {
        'min': 0.3277,
        'max': 0.5890
      },
      'a4': {
        'min': -0.2003,
        'max': 0.0602
      },
      'signalPower': 0.8901,
      'outputs': {
          0: 0.0,
          1: 1.0,
          2: 0.0,
          3: 0.0,
          4: 0.0,
          5: 0.0
      }
    },
    2: {
      'a1': {
        'min': -1.8022,
        'max': -1.6591
      },
      'a2': {
        'min': 0.3128,
        'max': 0.4710
      },
      'a3': {
        'min': 0.4905,
        'max': 0.6052
      },
      'a4': {
        'min': -0.2632,
        'max': -0.0814
      },
      'signalPower': 0.9488,
      'outputs': {
          0: 0.0,
          1: 0.0,
          2: 1.0,
          3: 0.0,
          4: 0.0,
          5: 0.0
      }
    },
    3: {
      'a1': {
        'min': -2.1035,
        'max': -1.9456
      },
      'a2': {
        'min': 0.6327,
        'max': 0.9701
      },
      'a3': {
        'min': 0.4601,
        'max': 0.6688
      },
      'a4': {
        'min': -0.2899,
        'max': -0.2875
      },
      'signalPower': 1.1469,
      'outputs': {
          0: 0.0,
          1: 0.0,
          2: 0.0,
          3: 1.0,
          4: 0.0,
          5: 0.0
      }
    },
    4: {
      'a1': {
        'min': -2.2974,
        'max': -2.1922
      },
      'a2': {
        'min': 1.1591,
        'max': 1.5157
      },
      'a3': {
        'min': 0.2509,
        'max': 0.4010
      },
      'a4': {
        'min': -0.2969,
        'max': -0.1108
      },
      'signalPower': 1.3278,
      'outputs': {
          0: 0.0,
          1: 0.0,
          2: 0.0,
          3: 0.0,
          4: 1.0,
          5: 0.0
      }
    },
    5: {
      'a1': {
        'min': -2.5220,
        'max': -2.3579
      },
      'a2': {
        'min': 1.5370,
        'max': 1.9656
      },
      'a3': {
        'min': -0.2942,
        'max': 0.0802
      },
      'a4': {
        'min': -0.2552,
        'max': -0.1471
      },
      'signalPower': 1.5206,
      'outputs': {
          0: 0.0,
          1: 0.0,
          2: 0.0,
          3: 0.0,
          4: 0.0,
          5: 1.0
      }
    }
}

filename = "generatedTrainingData.txt"

target = open(filename, 'w')
target.truncate()

target.write("fuzzifier: 4\n")
target.write("errorMargin: 0.01\n")
target.write("iterationLimit: 2000\n")
target.write("topology: 5 6 6\n")
target.write("learningRate: 0.95\n")
target.write("momentum: 0.1\n")

count = 0
while count <= 4800:
    count += 1

    currentMovementIndex = random.randint(0, 5)
    currentMovement = movement[currentMovementIndex % 6]

    target.write("in: %f %f %f %f %f\n" \
                 % (
                     random.uniform(currentMovement['a1']['min'], currentMovement['a1']['max']),
                     random.uniform(currentMovement['a2']['min'], currentMovement['a2']['max']),
                     random.uniform(currentMovement['a3']['min'], currentMovement['a3']['max']),
                     random.uniform(currentMovement['a4']['min'], currentMovement['a4']['max']),
                     currentMovement['signalPower']
                 ))
    target.write("out: %f %f %f %f %f %f\n" \
                 % (
                     currentMovement['outputs'][0],
                     currentMovement['outputs'][1],
                     currentMovement['outputs'][2],
                     currentMovement['outputs'][3],
                     currentMovement['outputs'][4],
                     currentMovement['outputs'][5],
                 ))


target.close()

filename = "liveTestingData.txt"

target = open(filename, 'w')
target.truncate()
count = 0

while count < 10000:
    count += 1

    currentMovementIndex = random.randint(0, 5)
    currentMovement = movement[currentMovementIndex % 6]
    target.write("in: %f %f %f %f %f\n" \
        % (
              random.uniform(currentMovement['a1']['min'], currentMovement['a1']['max']),
              random.uniform(currentMovement['a2']['min'], currentMovement['a2']['max']),
              random.uniform(currentMovement['a3']['min'], currentMovement['a3']['max']),
              random.uniform(currentMovement['a4']['min'], currentMovement['a4']['max']),
              currentMovement['signalPower']
          )
    )

    target.write("out: %f %f %f %f %f %f\n" \
        % (
              currentMovement['outputs'][0],
              currentMovement['outputs'][1],
              currentMovement['outputs'][2],
              currentMovement['outputs'][3],
              currentMovement['outputs'][4],
              currentMovement['outputs'][5],
          )
     )


target.close()