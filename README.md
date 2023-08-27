# Tuple Unpacking

Instructions: You are working on a mapping software. The map is stored as a list of points, where each item is represented as a tuple, containing the X and Y coordinates of the point.
You need to calculate and output the distance to the closest point from the point (0, 0).
To calculate the distance of the point (x, y) from (0, 0), use the following formula: √(x²+y²)

Pseudocode:





            BEGIN
              IMPORT math
              DECLARE points = [
                                    (12, 55),
                                    (880, 123),
                                    (64, 64),
                                    (190, 1024),
                                    (77, 33),
                                    (42, 11),
                                    (0, 90)
                                ]

              DECLARE x AND y to first point which written like this to access points[0] = (12, 55)
              DECLARE closest_point equals to mathematics square root of x-sqrd + y-sqrd

              FOR each x, y in points[1:]:
                DECLARE distance equals to mathematics square root of x-sqrd + y-sqrd
                IF distance is less than closest_point
                  closest_point equals to distance now
                ENDIF
              ENDFOR

              PRINT closest_point

            END
