import random

movement = {}

movement = {
    0: {
      'a1': {
        'min': -0.7,
        'max': -1.1
      },
      'a2': {
        'min': -0.25,
        'max': 0.0
      },
      'a3': {
        'min': 0.0,
        'max': 0.4
      },
      'a4': {
        'min': -0.1,
        'max': 0.3
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
        'min': -1.9,
        'max': -1.3
      },
      'a2': {
        'min': 0.0,
        'max': 0.5
      },
      'a3': {
        'min': 0.2,
        'max': 0.8
      },
      'a4': {
        'min': -0.25,
        'max': 0.1
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
        'min': -2,
        'max': -1.5
      },
      'a2': {
        'min': 0.25,
        'max': 0.5
      },
      'a3': {
        'min': 0.45,
        'max': 0.8
      },
      'a4': {
        'min': -0.3,
        'max': -0.1
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
        'min': -2.3,
        'max': -1.8
      },
      'a2': {
        'min': 0.5,
        'max': 1.0
      },
      'a3': {
        'min': 0.3,
        'max': 0.8
      },
      'a4': {
        'min': -0.17,
        'max': -0.25
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
        'min': -2.4,
        'max': -2
      },
      'a2': {
        'min': 1.0,
        'max': 1.7
      },
      'a3': {
        'min': 0.2,
        'max': 0.43
      },
      'a4': {
        'min': -0.32,
        'max': -0.09
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
        'min': -2.9,
        'max': -2.1
      },
      'a2': {
        'min': 1.45,
        'max': 2.1
      },
      'a3': {
        'min': -0.34,
        'max': 0.1
      },
      'a4': {
        'min': -0.3,
        'max': -0.12
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
target.write("topology: 5 6 6\n")
for currentMovementIndex in range (0, 12):
    currentMovement = movement[currentMovementIndex % 6]
    for x in range (0, 3600):
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