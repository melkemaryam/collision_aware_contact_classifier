# Summary of Grayscale Threshold Predictions

There were several trials, all tested on the training files for the neural network: 
* 0 (no contact)
* 1 (contact)
* 2 (collision)

Trials:
* and operator with all three pixel values
* or operator with all three pixel values
* grayscale value 1 [280, 32]
* grayscale value 2 [280, 280]
* grayscale vlaue 3 [280, 400]

Conclusion:
* using the Graysclae value for comparison, the best accuracies could be achieved:
    * no contact: 99.9%
    * contact: 28.3%
    * collision: 77.9%
    * hence, average accuracy: **68,7%**

## And operator

For no contact:
* **no contact: 1133 ==> 99.91181657848325%** 
* contact: 0 ==> 0.0% 
* collision: 0 ==> 0.0% 
* unknown: 1 ==> 0.08818342151675485% 

For contact:
* no contact: 204 ==> 17.989417989417987% 
* **contact: 3 ==> 0.26455026455026454%** 
* collision: 1 ==> 0.08818342151675485% 
* unknown: 926 ==> 81.65784832451499% 

For collision:
* no contact: 18 ==> 1.5873015873015872% 
* contact: 4 ==> 0.3527336860670194% 
* **collision: 50 ==> 4.409171075837742%** 
* unknown: 1062 ==> 93.65079365079364% 

## Or operator

For no contact:
* **no contact: 1134 ==> 100.0%** 
* contact: 0 ==> 0.0% 
* collision: 0 ==> 0.0% 
* unknown: 0 ==> 0.0%  

For contact:
* no contact: 967 ==> 85.27336860670194% 
* **contact: 149 ==> 13.139329805996471%**
* collision: 17 ==> 1.4991181657848323% 
* unknown: 1 ==> 0.08818342151675485%  

For collision:
* no contact: 538 ==> 47.44268077601411% 
* contact: 517 ==> 45.59082892416226% 
* **collision: 79 ==> 6.966490299823633%** 
* unknown: 0 ==> 0.0% 

## Grayscale Value 1

For no contact:
* **no contact: 1134 ==> 100.0%** 
* contact: 0 ==> 0.0% 
* collision: 0 ==> 0.0% 
* unknown: 0 ==> 0.0%  

For contact:
* no contact: 744 ==> 65.60846560846561% 
* **contact: 73 ==> 6.437389770723104%** 
* collision: 253 ==> 22.310405643738974% 
* unknown: 64 ==> 5.64373897707231%   

For collision:
* no contact: 422 ==> 37.213403880070544% 
* contact: 182 ==> 16.049382716049383% 
* **collision: 466 ==> 41.09347442680776%** 
* unknown: 64 ==> 5.64373897707231%

## Grayscale Value 2

For no contact:
* **no contact: 1134 ==> 100.0%** 
* contact: 0 ==> 0.0% 
* collision: 0 ==> 0.0% 
* unknown: 0 ==> 0.0%  

For contact:
* no contact: 579 ==> 51.05820105820106% 
* **contact: 229 ==> 20.19400352733686%** 
* collision: 158 ==> 13.932980599647266% 
* unknown: 168 ==> 14.814814814814813%    

For collision:
* no contact: 181 ==> 15.961199294532626% 
* contact: 708 ==> 62.43386243386243% 
* **collision: 160 ==> 14.109347442680775%** 
* unknown: 85 ==> 7.495590828924162% 

## Grayscale Value 3

For no contact:
* **no contact: 1133 ==> 99.91181657848325%** 
* contact: 0 ==> 0.0% 
* collision: 0 ==> 0.0% 
* unknown: 1 ==> 0.08818342151675485%   

For contact:
* no contact: 462 ==> 40.74074074074074% 
* **contact: 321 ==> 28.306878306878307%** 
* collision: 282 ==> 24.867724867724867% 
* unknown: 69 ==> 6.084656084656085%    

For collision:
* no contact: 103 ==> 9.082892416225748% 
* contact: 129 ==> 11.375661375661375% 
* **collision: 883 ==> 77.86596119929453%** 
* unknown: 19 ==> 1.6754850088183422% 