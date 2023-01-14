Question 2: Enzyme Kinetics

8.1: 
The law of mass action states that the rate of a chemical reaction is proportional to the product of the concentrations of the reactants raised to the power of their stoichiometric coefficients. Therefore, the four equations for the rate of changes of the four species in this simplified enzyme reaction are:

dE/dt= -k1* [E] * [S] + k2 * [ES]

dS/dt= -k1* [E] * [S] + k2 * [ES] + k3 * [ES]

dES/dt= k1* [E] * [S] - k2 * [ES] - k3 * [ES]

dP/dt= k3* [ES]

Where [E], [S], [ES], and [P] represent the concentrations of the enzyme E, substrate S, intermediate species ES, and product P respectively, and k1, k2, k3 are the forward rate, reverse rate, and product formation rate respectively.

8.2

![Image text](https://raw.githubusercontent.com/ZhenghongLei2000/Programme_questions-AY23/main/Question2/Q2%208.2.png)

8.3 we can use the Michaelis-Menten equation. This equation describes the velocity of the enzymatic reaction as a function of the substrate concentration. The equation is:

V = V_m*( [S] / (K_m+ [S]))

Where V_m is the maximum velocity of the reaction, [S]  is the substrate concentration, and K_m is the Michaelis constant, which represents the substrate concentration at which the reaction reaches half of its maximum velocity.

In the equation, when the concentrations of S are small, the velocity V increases approximately linearly as the concentration of S increases. As the concentration of S increases, the velocity V will approach the maximum value, V_m.

To find V_m from the plot, we can look for the point where the velocity V saturates and stops increasing. This will be the maximum value of V, or V_m

![Image text](https://raw.githubusercontent.com/ZhenghongLei2000/Programme_questions-AY23/main/Question2/Q2%208.3.png)

Take the value of 8.2 as example:

Km = k2/k3 =  (600/min)/(150/min)= 4 µM

V_m  = k3 * [E] = 150/min * 1 µM = 150 µM/min

V = 150 µM/min * (S/(4 µM + S))

The velocity V saturates to a maximum value of 150 µM/min, which is V_m.
