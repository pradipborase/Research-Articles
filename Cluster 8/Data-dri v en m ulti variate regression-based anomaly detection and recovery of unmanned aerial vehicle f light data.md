# Data-dri v en m ulti variate regression-based anomaly detection and recovery of unmanned aerial vehicle f light data.pdf

## Page 1

Journal of Computational Design and Engineering , 2024, 11 , 176–193 
DOI: 10.1093/jcde/qwae023 
Ad v ance access publication date: 12 March 2024 
Research Article 
Data-dri v en m ulti variate regression-based anomaly 
detection and recovery of unmanned aerial vehicle 
flight data 
Lei Yang 1 , Shaobo Li 1 ,2 , * , Chuanjiang Li 2 , * and Caichao Zhu 3 
1 School of Mechanical Engineering, Guizhou University, Guiyang 550025, China. 
2 State Key Laboratory of Public Big Data, Guizhou University, Guiyang 550025, China. 
3 State Key Laboratory of Mechanical Transmission, Chongqing University, Chongqing 400044, China 
∗Correspondence: shaobo Li, lishaobo@gzu.edu.cn ; Chuanjiang Li, licj@gzu.edu.cn 
Abstract 
Flight data anomaly detection is crucial for ensuring the safe operation of unmanned aerial vehicles (UAVs) and has been exten- 
si v el y studied. Howev er, the accurate modeling and anal ysis of flight data is c hallenging due to the influence of r andom noise . Mean- 
while, existing methods are often inadequate in parameter selection and feature extraction when dealing with large-scale and high- 
dimensional flight data. This paper proposes a data-driven multivariate regression-based fr amew ork considering spatio-temporal 
correlation for UAV flight data anomaly detection and r ecov er y, whic h inte gr ates the tec hniques of correlation analysis (CA), one- 
dimensional convolutional neural network and long short-term memory (1D CNN-LSTM), and error filtering (EF), named CA-1DCL-EF. 
Specifically, CA is first performed on original UAV flight data to select parameters with correlation to reduce the model input and 
avoid the negative impact of irrelevant parameters on the model. Next, a regression model based on 1D CNN-LSTM is designed to 
fully extract the spatio-temporal features of UAV flight data and realize parameter mapping. Then, to overcome the effect of random 
noise, a filtering technique is introduced to smooth the errors to improve the anomaly detection performance . F inally, tw o common 
anomaly types are injected into real UAV flight datasets to verify the effectiveness of the proposed method. 
Ke yw ords: unmanned aerial v ehicle, anomal y detection, data r ecov er y, m ulti v ariate r egr ession, err or filtering, corr elation anal ysis 
1. Introduction 
Unmanned aerial vehicles (UAVs) have expanded from military 
to civilian applications (Liang et al., 2022 ), such as traffic (Outay 
et al., 2020 ), a gricultur e (Liu et al. , 2021 ; Maes et al. , 2019 ), build- 
ing inspection and surveillance (Jing & Shimada, 2017 ), and disas- 
ter rescue (Hildmann & K o vacs , 2019 ; Wang et al. , 2022 ). W ith the 
incr easing a pplication ar eas, the global UAV market is projected 
to r eac h USD 45.8 billion by 2025 and USD 56.18 billion by 2027 
(Ahmad et al., 2022 ). Despite their promising potential, UAVs face 
inher ent c hallenges contributing to a higher accident rate than 
manned aircraft (K. He et al., 2022 ; Wang et al., 2020 ; Yang et al., 
2023 ; Zhai & Ye, 2020 ). Issues like limited r eal-time contr ol, size 
constr aints, and de v elopment costs may lead to se v er e dama ge 
or loss . T he safety and reliability of UAVs have been the subject 
of extensive research and remain a paramount concern (Chen 
et al., 2022 ). Flight data play a crucial role in understanding the 
status and performance of UAVs . T hus , flight data anomaly de- 
tection is crucial for enhancing the safety and reliability of UAVs 
and fostering the advancement and widespread adoption of UAV 
technology. 
UAV flight data anomaly detection a ppr oac hes mainl y include 
knowledge-based, model-based, and data-driven methods (Yang 
et al., 2023 ; Zhong et al ., 2022 ). Knowledge-based methods utilize 
pr edefined c har acteristics and rules of normal UAV flight data to 
identify anomalies in new flight data, including hidden anomalies 
that may be challenging to detect using other methods (Theissler, 
2017 ). Ho w e v er, the construction of models or rule bases for nor- 
mal data in knowledge-based methods relies heavily on expert 
knowledge, which is limited by the expertise and knowledge le v el 
of the experts . Hence , these methods ha v e been primaril y uti- 
lized in earl y r esearc h (Bu et al ., 2017 ; Qi et al., 2007 ). Model-based 
a ppr oac hes utilize mathematical models to describe the differ- 
ences between normal and abnormal behaviors of UAVs and em- 
ploy machine learning algorithms to learn and identify these dif- 
fer ences (Fr eeman et al., 2013 ). T hese methods in volv e tr aining 
the model with historical flight data to learn the features of nor- 
mal behavior. Subsequentl y, ne w flight data ar e inputted into the 
model for prediction, and anomalies are determined based on 
the pr ediction err ors (Abbaspour et al., 2017 ; López-Estr ada et al., 
2016 ). Despite the adv anta ges of model-based a ppr oac hes in in- 
ter pr etability, computational cost, and reliability, they encounter 
challenges in accurately constructing mathematical models due 
to the complexity of the UAV system. These challenges may lead 
to model mismatc hes, r esulting in high err or r ates and limited 
generalization ability (Liang et al., 2022 ; Wang et al., 2019 ). 
Unlike knowledge- and model-based a ppr oac hes, data-driv en 
a ppr oac hes utilize massive UAV flight data to effectiv el y learn and 
detect anomalies by employing deep learning or machine learning 
techniques without relying on expert knowledge or establishing 
complex physical models. Commonly used deep learning-based 
Recei v ed: October 17, 2023. Revised: Mar c h 7, 2024. Accepted: Mar c h 7, 2024 
© The Author(s) 2024. Published by Oxford Uni v ersity Pr ess on behalf of the Society for Computational Design and Engineering. This is an Open Access article 
distributed under the terms of the Cr eati v e Commons Attribution-NonCommercial License ( https://cr eati v ecommons.org/licenses/by-nc/4.0/ ), which permits 
non-commer cial re-use , distribution, and r e pr oduction in any medium, pr ovided the original work is pr operl y cited. For commercial r e-use, please contact 
journals.permissions@oup.com 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 2

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 177 
anomaly detection methods mainly include long short-term 
memory (LSTM) network (Gu et al., 2022 ; Jia et al., 2023 ) or its 
combination with other models, such as autoencoder (AE, Bae 
& J oe , 2020 ; Yang et al., 2023 ) and principle component analy- 
sis (PCA, Wang et al., 2020 ) to impr ov e the accur ate identifica- 
tion and modeling capability of anomalous behavior of UAV flight 
data. Yang et al. ( 2023 ) proposed an unsupervised LSTM-AE data- 
driven method for accurate anomaly detection of a subset of UAV 
height classes. Bae and Joe ( 2020 ) utilized LSTM-AE and AE mod- 
els with good anomaly detection performance in UAV environ- 
ment. Zhong et al. ( 2022 ) proposed a spatio-temporal correlation- 
based LSTM (STC-LSTM) data-driv en method to ac hie v e anomal y 
detection of UAV flight data with multiple anomaly types. Wang 
et al. ( 2019 ) applied the LSTM with residual filtering method to 
the anomaly detection of UAV flight data and verified the effec- 
tiveness of their method using r oll r ate as the detected parame- 
ter. Wang et al. ( 2020 ) proposed a PCA-LSTM-based model to real- 
ize real-time fault detection of UAVs under on-board constraints. 
In addition, ther e ar e some mac hine learning-based anomal y de- 
tection methods, such as kernel principle component analysis 
(KPCA, Duan et al., 2017 ), PCA (Alos et al., 2020 ), r ele v ance v ec- 
tor machine (R VM, W ang et al., 2019 ), k -nearest neighbor (KNN, 
Alos & Dahrouj, 2020 ; Liu & Ding, 2015 ), and support vector ma- 
c hine (SVM, Br onz et al., 2020 ; P an et al., 2020 ). Duan et al. ( 2017 ) 
proposed a KPCA-based data-driven method and obtained sat- 
isfactory performance on simulated UAV sensor data. Alos et al. 
( 2020 ) used PCA to detect anomalies in anomalous flights with- 
out false alarms. Alos and Dahrouj ( 2020 ) proposed a data-driven 
a ppr oac h for detecting contextual faults, which was centered 
on the use of dynamic linear r egr ession to estimate the value 
of the focus attribute and classifying anomalous data based on 
KNN. Liu and Ding ( 2015 ) first indexed the historical flight data 
thr ough k -dimensional (KD) tr ee, and then utilized KNN to iden- 
tify anomalous data and provide reasonable prediction values. 
Bronz et al. ( 2020 ) used SVM to construct optimal hyperplanes in 
high-dimensional spaces to classify abnormal and normal data. 
Pan et al. ( 2020 ) proposed an enhanced semi-supervised SVM 
method integr ating activ e learning by comparing pr edicted v al- 
ues and uncertainty intervals for anomaly detection in UAV flight 
data. 
The aforementioned publications highlight that researchers 
have made significant progress in utilizing data-driven methods 
for anomaly detection in UAV flight data. Ho w ever, there are still 
se v er al shortcomings and challenges: 
(i) Most existing deep and machine learning-based UAV flight 
data anomaly detection methods often lack effective pa- 
r ameter selection, whic h may limit their pr actical a pplica- 
bility (Bae et al., 2020 ; Jia et al., 2023 ). The reason for this 
limitation is that some unrelated flight parameters may 
not positiv el y affect the model. While PCC-based par ame- 
ter selection method may lose the beneficial effects of k e y 
nonlinear parameters on the model (Alos et al., 2020 ; Wang 
et al., 2019 ). 
(ii) Curr ent methods ar e mainl y based on LSTM for model- 
ing flight data. Ho w e v er, for complex data with spatio- 
tempor al c har acteristics and m ultipar ameter inter actions 
like UAV flight data, r el ying on LSTM alone to extract fea- 
tures may have some limitations (Gu et al., 2022 ; Jia et al., 
2023 ; Wang et al., 2019 ; Zhong et al ., 2022 ). 
(iii) Sensor errors , external en vironment, and other factors 
cause random noise in the real UAV flight data. Methods 
like STC-LSTM (Zhong et al ., 2022 ) and R VM (W ang et al., 
2019 ) may lead to higher false detection rates, as they do 
not account for random noise. 
(iv) Methods like SVM (Bronz et al., 2020 ), KPCA (Duan et al., 
2017 ), and PCA (Alos et al., 2020 ) demonstrate relatively 
good anomaly detection performance, they often overlook 
the crucial aspect of data r ecov ery. 
To address the aforementioned issues and challenges, this pa- 
per proposes a data-driven multivariate regression-based frame- 
work CA-1DCL-EF for UAV flight data anomaly detection and re- 
cov ery. First, a corr elation anal ysis (CA) method is intr oduced to 
select flight parameters with correlation as model input, mit- 
igating the adverse effects of irr ele v ant par ameters on model 
performance. Second, by fully utilizing the advantages of one- 
dimensional convolutional neural network (1D CNN) and LSTM 
in local featur e extr action and capturing time-dependence, a re- 
gression model based on 1D CNN-LSTM is designed to capture the 
spatio-tempor al featur es of the data compr ehensiv el y. Finall y, to 
reduce the impact of random noise, an error filtering (EF) tech- 
nique is introduced to smooth the errors and improve the model’s 
anomaly detection performance. Specifically, compared with pre- 
vious studies, this paper makes new contributions in the following 
aspects: 
(i) As an alternative to existing methods, a multivariate re- 
gression model based on 1D CNN-LSTM is designed to fully 
extr act the spatio-tempor al featur es of UAV flight data by 
combining the adv anta ges of 1D CNN in local feature ex- 
traction and LSTM in temporal feature extraction. 
(ii) A no vel C A-1DCL-EF framework for UAV flight data 
anomaly detection and recovery is proposed, which in- 
cludes CA, EF, anomal y detection, and data r ecov ery, and 
provides a more comprehensive solution to the practical 
problems faced in UAV anomaly detection research. 
(iii) Experiments on real high-dimensional UAV flight datasets 
and detailed e v aluations and comparisons with baseline 
methods are conducted; thus, the effectiveness of CA- 
1DCL-EF is verified. 
The rest of this paper is structured as follows. Section 2 provides 
an ov ervie w of the fundamental theory. Section 3 details the pr o- 
posed fr ame work, outlining its k e y components and methodology. 
Section 4 presents the experimental results and analysis obtained 
by a ppl ying the fr ame work. Section 5 summarizes this work and 
discusses possible future research directions. 
2. Preliminaries 
2.1. Maximal information coefficient 
The maximal information coefficient (MIC) is a widely used 
nonparametric method for quantifying the correlation between 
two variables (Reshef et al., 2011 ). It measures the correla- 
tion between variables without making assumptions about spe- 
cific functional forms or linear r elationships. MIC v alues r ange 
from 0 to 1 and demonstrate symmetry. Larger MIC values in- 
dicate stronger correlations between the variables. When the 
MIC value is equal to 0, it indicates that the variables are in- 
dependent of each other. Given a grid G of size x × y and 
a finite set of ordered pairs ( A, B ) = ({ a i , b i } , i = 1 , 2 , . . . , n ) , n is 
the variable length. When calculating MIC, mutual informa- 
tion (MI) needs to be calculated first, which is defined as 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 3

178 | UAV flight data anomaly detection and recovery 
Figure 1: 1D CNN structure diagram. 
follows: 
MI (A,B ) = 
 
a ∈ A 
 
b∈ B 
p (a, b ) lg p (a, b ) 
p (a ) p (b ) 
(1) 
where MI ( A , B ) is MI of A and B , p ( a , b ) signifies the joint probability 
density of A and B , and p ( a ) and p ( b ) refer to the mar ginal pr oba- 
bility densities of A and B , r espectiv el y. The cor e principle of MIC 
entails measuring the correlation between two variables by max- 
imizing MI, which is defined as follows: 
MI ∗(D, x, y ) = max MI(D | G ) 
(2) 
where MI ∗( D , x , y ) denotes the maximum MI of D on the grid G . 
D | G indicates that D is being divided using the grid G . D is the data, 
here it denotes ( A , B ). In this process, there is involvement with the 
feature matrix concerning D , enabling MIC to assess MI between 
variables in different grid partitions to determine the maximum 
MI value . T he feature matrix is defined as follows: 
MI (D ) x,y = MI ∗(D, x, y ) 
log min { x, y } 
(3) 
where log min{ x , y } is the element of the normalized feature ma- 
trix. Ther efor e, based on equation ( 3 ), the MIC can be defined as 
follows: 
MI C (D ) x,y = max 
xy<C(n ) { M (D ) x,y } 
(4) 
where C ( n ) is the maximum value of the grid G and w (1) ≤C(n ) ≤
O ( n 1 −ε ) , 0 < ε < 1. ε is a positive number less than 1, used to adjust 
the upper limit of C ( n ). w (1) is a parameter related to the sample 
size and is typically a small positive number. 
2.2. One-dimensional convolutional neural 
network 
The 1D CNN (Kir an yaz et al. , 2021 ; Li et al. , 2022 ) is utilized to 
extr act featur es fr om differ ent positions of the input signal us- 
ing sliding windows. It typically consists of convolutional, pooling, 
and fully connected la yers , as shown in Fig. 1 . 
T he con volution la yer is a fundamental component of the 1D 
CNN arc hitectur e, extr acting local features from the input data. 
Its calculation is shown as follows: 
χl 
j = g 
⎛ 
⎝  
i ∈ F j 
x l−1 
i 
· k l 
i j + b l 
j 
⎞ 
⎠ 
(5) 
Figure 2: LSTM structure diagram. 
where χl+1 
j is the j th element of the in the l th layer of the input fea- 
ture F j . k , b , and g ( ·) are the con volution kernel, bias , and the non- 
linear activation function of the convolution layer, r espectiv el y. 
The pooling layer plays a crucial role in reducing the number of 
parameters in the model while preserving essential features and 
enhancing its generalization capability, which is defined as fol- 
lows: 
χl+1 
j 
= Pooling (χl 
j ) 
(6) 
where χl+1 
j 
denotes the j th element of the l + 1th layer and 
Pooling ( ·) is the pooling oper ation. The full y connected layer is 
computed as follows: 
χl = f(w l x l−1 + b l ) 
(7) 
where ω l , b l , and f ( ·) are the weights , bias , and nonlinear activation 
functions of the fully connected layer, respectively. 
2.3. Long short-term memory 
LSTM is a variant of recurrent neural networks that excels at cap- 
turing long-term dependencies (Gr av es, 2012 ). Ther e ar e for get 
gate f t , input gate i t , output gate o t , and memory cell of LSTM, 
as shown in Fig. 2 . f t is the initial recipient of information, deter- 
mining which piece of historical information to retain or forget 
in the current state. Suppose the input data are x t at time t , f t is 
defined as follows: 
f t = σ (w h f h t−1 + w x f x t + b f ) 
(8) 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 4

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 179 
Figur e 3: T he proposed C A-1DCL-EF fr ame work. 
where σ is the activation function, w h f and w x f are the weights of 
f t . b f is the bias of f t . h t−1 denote the cell state and output vector at 
time t −1. i t is used to control which information from the current 
input to the network flows into the memory cell, which is defined 
as follows: 
i t = σ (w hi h t−1 + w xi x t + b i ) 
(9) 
 
c t = tanh (w xc x t + w hc h t−1 + b c ) 
(10) 
c t = f t ⊗c t−1 + i t ⊗ 
c t 
(11) 
where w hi and w xi are the weights of i t . b i is the bias of i t . ˜ 
c t is the 
intermediate state parameter used for updating at time t . w hc and 
w xc are the weights of ˜ 
c t . b c is the bias of ˜ 
c t . tanh is the activation 
function. c t−1 denotes the output vector at time t −1. ࣹdenotes 
the dot product. o t controls which part of the memory cell will be 
output at time t . It is defined as follows: 
o t = w ho h t−1 + w xo x t + b o 
(12) 
h t = o t ⊗tanh (c t ) 
(13) 
where w ho and w xo are the weights of o t . b o is the bias of o t . 
3. Methodology Fr ame work 
This pa per pr oposes a data-driv en m ultiv ariate r egr ession-based 
fr ame work CA-1DCL-EF considering spatio-tempor al corr elation, 
as shown in Fig. 3 . It innov ativ el y integr ates CA, 1D CNN-LSTM, 
and EF. First, the raw UAV flight data are normalized to elimi- 
nate the effect of different magnitudes . Second, MIC-based C A is 
performed to select parameters with correlation, which are then 
used as inputs to the model. Then, 1D CNN-LSTM model is trained 
and e v aluated using tr aining and test sets. Finall y, the tr aining er- 
r ors ar e smoothed to obtain the anomaly determination thresh- 
old. Anomaly detection is achieved by comparing the smoothed 
test errors with the threshold, and data recovery is achieved by re- 
placing the anomalous data with the predicted data. Specifically, 
the pr oposed fr ame work CA-1DCL-EF mainl y includes thr ee parts: 
data pr epr ocessing, par ameter selection, and anomal y detection 
and r ecov ery, whic h ar e described in detail in this section. 
3.1. Data preprocessing 
The original UAV flight data are normalized using the maximum–
minimum normalization method (Jahan & Edwards, 2015 ). It ad- 
justs eac h featur e r ange to [0,1] to facilitate the model to learn the 
features better. It is defined as follows: 
x ′ = x −x min 
x max −x min 
(14) 
where x represents the original data and x ′ the normalized data. 
x max and x min are the maximum and minimum values of x , respec- 
tiv el y. 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 5

180 | UAV flight data anomaly detection and recovery 
Figure 4: Schematic diagram of different grid division schemes. 
3.2. MIC-based parameter selection 
Since ther e ar e numer ous flight par ameters, it is necessary to per- 
form parameter selection to reduce the risk of model underfitting. 
Ho w e v er, linear and nonlinear correlation parameters in the flight 
data need to be fully considered in the parameter selection pro- 
cess to avoid the loss of critical parameters that may positiv el y af- 
fect the model performance. Compared with PCC, MIC can capture 
both linear and nonlinear correlations between parameters. An il- 
lustr ativ e example is presented in Fig. 4 , where different-colored 
lines r epr esent distinct grid division schemes and ( A, B ) contains 
10 ordered pairs. Considering the grid scheme divided by the red 
lines as an example, the joint and boundary probability densities 
of variables ( A, B ) are as follows: p (left, up) = 0.2, p (right, up) = 0.3, 
p (left, down) = 0.3, p (right, down) = 0.2, p (left) = 0.5, p (right) = 0.5, 
p (up) = 0.5, and p (down) = 0.5. The MI under this scheme can be 
calculated according to equation ( 1 ), i.e., 
MI (A,B ) = 0 . 2 ∗

log 

0 . 2 
0 . 5 ∗0 . 5 
	
+ log 

0 . 2 
0 . 5 ∗0 . 5 
		
+ 0 . 3 ∗

log 

0 . 3 
0 . 5 ∗0 . 5 
	
+ log 

0 . 3 
0 . 5 ∗0 . 5 
		
= 0 . 0087 
(15) 
The MI values of other grid sc hemes, suc h as those divided 
by orange and black lines, are also computed. The grid division 
scheme with the highest MI value is chosen as the final scheme 
based on the calculation described in equation ( 2 ). Subsequently, 
the maxim um v alue is normalized using equation ( 3 ), resulting 
in the maxim um MI v alue, denoted as MIC. A corr elation be- 
tween variables A and B exists when MIC is greater than or equal 
to γ . The calculation of MIC can be performed using the MINE 
pac ka ge (Reshef et al., 2012 ), and its pr ocedur e is outlined in 
Algorithm 1. 
Algorithm 1 : MIC calculation process. 
3.3. C A-1DCL-EF-based anomal y detection and 
recovery 
3.3.1. Model ar c hitecture 
Figure 5 shows the structure diagram of the designed 1D CNN- 
LSTM r egr ession model. 1D CNN ca ptur es local features of the 
input data through con volutional operations , effecti vely ad dress- 
ing local correlations in the time series and reducing the model’s 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 6

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 181 
Figur e 5: T he designed 1D CNN-LSTM structur e dia gr am. 
Table 1: Input and output shapes of each layer. 
La y er 
Input shape 
Output shape 
Con volution la yer 
(None, S , n ) 
(None, S , 128) 
Max pooling layer 
(None, S , 128) 
(None, 1, 128) 
Dropout layer 1 
(None, 1, 128) 
(None, 1, 128) 
LSTM layer 1 
(None, 1, 128) 
(None, 1, 64) 
Dropout layer 2 
(None, 1, 64) 
(None, 1, 64) 
LSTM layer 2 
(None, 1, 64) 
(None, 1, 32) 
LSTM layer 3 
(None, 1, 32) 
(None, 1, 16) 
LSTM layer 4 
(None, 1, 16) 
(None, 8) 
Fully connected layer 
(None, 8) 
(None, 1) 
parameter count. LSTM utilizes its gate mechanism to regulate 
the information flow, which can capture long-term dependencies. 
Combining the strengths of 1D CNN and LSTM, 1D CNN-LSTM can 
mor e compr ehensiv el y ca ptur e spatio-tempor al featur es in flight 
data and impr ov e the pr ediction ability of time series data. Specifi- 
cally, 1D CNN-LSTM contains a convolutional layer, a max pooling 
lay er, tw o dropout layers, four LSTM layers, and a fully connected 
la yer. T he input and output shapes of each layer are shown in Ta- 
ble 1 . 
3.3.2. Model training 
The UAV flight parameters with correlation are first normalized 
using equation ( 14 ) before the model training. Then, the normal- 
ized parameters are reconstructed to match the input format of 
the model, which is defined as follows: 
X(t) = 
⎡ 
⎢ 
⎢ 
⎢ 
⎢ 
⎣ 
x t−1 
1 , x t−2 
1 , ..., x t−S 
1 
x t−1 
2 , x t−2 
2 , ..., x t−S 
2 
. . . 
x t−1 
n , x t−2 
n , ..., x t−S 
n 
⎤ 
⎥ 
⎥ 
⎥ 
⎥ 
⎦ 
, Y( t) = y ( t) 
(16) 
where X ( t ) is the model input, S is the sliding window, and n is 
the number of parameters with correlation, respectively. Figure 6 
shows the schematic diagram of the sliding window. Through ex- 
tensiv e explor atory experiments, combined with data c har acter- 
ization. In this paper, S was set to 5. Y ( t ) and y ( t ) are the target 
values of the model output and the detected parameter at time t . 
The pr edicted v alue ˆ 
Y ( t ) of the model is obtained after inputting 
X ( t ) into the model. The objective of model training is to minimize 
the error between ˆ 
Y (t) and Y(t) , which is defined as follows: 
J = 1 
l 
 l 
i =1 ( ˆ 
y i −y i ) 2 
(17) 
where ˆ 
y i and y i are the i th elements of ˆ 
Y (t) and Y(t) , r espectiv el y, 
and l is the sample length. 
Tw o dropout lay ers are added to mitigate the model overfitting 
phenomenon. In each training iteration, the dropout layer ran- 
domly discards some neurons from the previous layer with a cer- 
tain probability. This helps to alleviate the complex collaborative 
r elationships between neur ons, thus enabling the model to learn 
mor e r obust featur es and impr oving the model’s gener alization 
ability (Tan et al., 2018 ). The training process is shown in Algo- 
rithm 2. 
Algorithm 2 : Model training process. 
3.3.3. Anomaly detection and data r ecover y 
For the training and test sets X (t) tr and X (t) te , the ˆ 
Y (t) tr and ˆ 
Y (t) te 
are obtained after the r egr ession of the 1D CNN-LSTM model, 
which can be defined as follows: 
ˆ 
Y (t) tr = f 1 D CNN −LSTM ( X ( t) tr ) 
(18) 
ˆ 
Y (t) te = f 1 D CNN −LSTM ( X ( t) te ) 
(19) 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 7

182 | UAV flight data anomaly detection and recovery 
Figur e 6: T he sc hematic dia gr am of the sliding window. 
Figure 7: Example of data smoothing using EWMA. 
where ˆ 
Y (t) tr and ˆ 
Y (t) te are the predicted values of the training 
and test sets, r espectiv el y. f 1 D C N N −LSTM (·) is the mapping function. 
Then, the errors e tr and e te of the training and test sets can be 
defined as follows: 
e tr = ( Y ( t) tr −ˆ 
Y ( t) tr ) 
2 
(20) 
e te = ( Y ( t) te −ˆ 
Y ( t) te ) 
2 
(21) 
where Y (t) tr and Y (t) te are the target values of the training and 
test sets, r espectiv el y. To mitigate the impact of random noise in 
the original UAV flight data, the exponentially weighted moving 
av er a ge (EWMA) method is emplo y ed (Lucas & Saccucci, 1990 ). 
EWMA a pplies an exponentiall y weighted av er a ge oper ation to 
the original time series data, assigning weights to each data point 
based on an exponential function. The calculation of EWMA can 
be defined as follows: 
e s 
i = αe s 
(i −1) + (1 −α) e i 
(22) 
where e s 
i is the i th smoothed error value, α is the adjustable weight 
parameter, and e i is the i th actual error value. Figure 7 shows an 
example of data smoothing using EWMA. The points present in 
the data that change drastically can be filtered out by EWMA and 
retain the most valuable and critical information. 
The e s 
tr and e s 
te are obtained after smoothing e tr and e te , respec- 
tiv el y, using equation ( 22 ). Then, anomaly detection can be defined 
as follows: 
Anomaly = 
 
1 , e s 
te > ¯e s 
tr 
0 , e s 
te < ¯e s 
tr 
(23) 
where ¯e s 
tr is the av er a ge v alue of e s 
tr , 1 indicates abnormal, and 0 
indicates normal. For data r ecov ery, the ˆ 
Y (t) te shown in equation 
(19) is the r ecov ery v alue. 
4. Experiments 
4.1. Data description 
The UAV flight datasets used in this paper were collected by the 
University of Minnesota (Ta ylor, 2013 , 2014 ). T hey collected flight 
data fr om v arious types of UAVs, and data fr om m ultiple flights 
performed by the same UAV type . T hese datasets ha v e been widel y 
used in r esearc h on the anomal y detection of UAV flight data (Y. 
He et al., 2017 ; Pan, 2017 , 2018 ; Yang et al., 2023 ). Specifically, the 
Thor Flight 98 and Thor Flight 104 datasets used in this study are 
r ecorded data fr om the 98th and 104th flights of the Thor UAV. 
Each dataset comprises 84 parameters sampled at a frequency of 
50 Hz. The length of each parameter in the Thor Flight 98 dataset 
and Thor Flight 104 dataset is 21 015 and 25 836, r espectiv el y. This 
paper uses the flight data from the Thor UAV during le v el flight 
with 16 000 data sampling points. 
Since anomaly data are difficult to obtain, this paper uses 
anomaly injection method to generate anomaly data. Specifically, 
two common types of anomalies in UAVs are considered: bias 
and drift anomalies, shown in equations ( 24 ) and ( 25 ), r espectiv el y 
(Freeman et al., 2013 ; Qi et al., 2013 ). The bias anomaly occurs when 
the UAV fails to maintain the expected trajectory, position, or atti- 
tude due to fixed factors, such as sensor errors , en vironmental dis- 
turbances, or po w er system issues, making the UAV flight data de- 
viate consistentl y fr om the anticipated v alues . T he drift anomaly 
involv es a gr adual de viation of UAV flight data from the intended 
trajectory or position, typically caused by dynamic factors, such 
as control system instability, attitude inaccuracies, or variations 
in wind speed. 
y (t) bias = y (t) + μ
(24) 
wher e y (t) ar e the original flight data, μ is a constant, and t is a 
period of time. 
y (t) drift = y (t) + θ(t) 
(25) 
where θ(t) is a constant or a function of a period of time t . 
NAV north velocity (NAVVN) is a crucial UAV parameter that 
can impr ov e the accur acy and r eliability of UAV na vigation. T here- 
for e, this pa per selects NAVVN as the detected par ameter to v erify 
the model’s performance. Figure 8 illustrates the flight datasets 
with injected bias and drift anomalies, and the data division. The 
anomaly injection range is [14 400:16 000]. For the bias anomaly, 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 8

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 183 
Figure 8: Flight datasets with injected bias and drift anomalies, and the data division. 
Figure 9: Visualization of correlation coefficient results based on PCC and MIC for Thor Flight 98 dataset. 
the value of μ is set to 4. Regarding the drift anomaly, 1600 points 
ar e e v enl y sampled fr om the r ange [4,5] using the linespace func- 
tion and added to the corresponding points within the interval 
[14 400:16 000]. The training set comprises the range [0:12 800], 
which accounts for 80% of the dataset, while the test set consists 
of the range [12 800:16 000], representing 20% of the dataset. 
4.2. Experimental set-up 
In the experiments, the operating system is Windows 10 (64-bit) 
and an AMD Ryzen 5 3600 6-Core @3.6 GHz processor is utilized 
for deep learning tasks. As the deep learning fr ame work, Tensor- 
Flow version 2.12.0 is chosen. During model training, the follow- 
ing hyper par ameter settings ar e used: a learning r ate of 0.001, a 
batch size of 128, a training epoch of 100 periods, and a dropout 
rate of 0.1. For the optimizer, the Adam optimizer is used to tune 
the model parameters. 
4.3. The results of MIC-based parameter 
selection 
After removing redundant parameters, 51 parameters are used for 
C A. Taking T hor Flight 98 dataset as an example, Fig. 9 shows the 
visualization of its correlation coefficient results based on MIC 
and PCC. Darker colors indicate stronger correlations and vice 
versa, with MIC displaying a greater number of darker grids com- 
pared with PCC. Table 2 shows the correlation coefficients of Thor 
Flight 98 dataset based on MIC and PCC between the detected pa- 
rameter NAVVN. Although PCC has high correlation coefficients 
between parameters with strong linear correlation, it is worth not- 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 9

184 | UAV flight data anomaly detection and recovery 
Table 2: Flight parameters with correlation to NAVVN in Thor 
Flight 98 dataset. 
Name 
Description 
Unit 
PCC 
MIC 
alt 
GPS altitude (WGS84) m 
0.02 
0.87 
ax_bias 
Accelerometer bias, 
X -axis 
rad/s 
0.11 
0.88 
ay_bias 
Accelerometer bias, 
Y -axis 
rad/s 
0.11 
0.85 
az_bias 
Accelerometer bias, 
Z -axis 
rad/s 
0.03 
0.86 
GPS_TOW 
Time of week from GPS s 
0.10 
0.89 
hx 
X-axis magnetic field 
Gauss 
0.85 
0.62 
lat 
GPS latitude 
deg 
0.10 
0.85 
lon 
GPS longitude 
deg 
0.55 
0.88 
psi 
Euler roll angle 
rad 
0.10 
0.80 
p_bias 
Gyro bias, X -axis (roll) rad/s 
0.12 
0.88 
q_bias 
Gyro bias, Y -axis (pitch) rad/s 
0.10 
0.80 
r_bias 
Gyro bias, Z -axis (yaw) rad/s 
0.10 
0.88 
vd 
GPS down velocity 
m/s 
0.36 
0.87 
ve 
GPS east velocity 
m/s 
0.03 
0.88 
vn 
GPS north velocity 
m/s 
0.95 
0.89 
ing that more accurately MIC captures the nonlinear correlations 
between parameters. In this work, the correlation determination 
threshold γ is set to 0.6, which is derived from previous research 
and experience (Alos et al., 2020 ; Yang et al., 2023 ; Zhong et al ., 
2022 ). Based on the MIC results, 15 parameters associated with 
NAVVN are selected as input parameters for the model. In order to 
clearl y demonstr ate the distribution status and probability den- 
sity of the used UAV flight datasets, the normalized parameter 
featur es ar e visualized using violin plots, as shown in Fig. 10 . The 
original range of values for each parameter feature is shown in 
the black boxes in Fig. 10 . 
4.4. The results of CA-1DCL-EF-based anomaly 
detection and recovery 
4.4.1. Evaluation metrics 
Anomaly detection focuses on the ability of the model to find 
and identify anomalies . T he true positive rate (TPR), false posi- 
tiv e r ate (FPR), and accur acy (ACC) r ate (Miao et al., 2018 ; Wang 
et al., 2019 ) are used to evaluate anomaly detection performance 
metrics . Data reco very aims to mitigate the effects of anomalies 
and return to safe flight conditions on time . T he mean absolute er- 
ror (MAE) and mean square error (MSE) are used to evaluate data 
r ecov ery performance (Hodson et al., 2022 ; Sun et al., 2019 ). The 
larger TPR and ACC values and the smaller FPR value indicate 
better model anomaly detection performance . T he smaller MAE 
and MSE values indicate better model data r ecov ery performance. 
Their calculation formulas are shown in equations ( 26 –30 ): 
T PR = 
T P 
T P + F N × 100% 
(26) 
F PR = 
F P 
T N + F P × 100% 
(27) 
ACC = 
T P + T N 
T P + T N + F P + F N × 100% 
(28) 
MAE = 1 
L 
L 
 
i =1 
| y i −ˆ 
y i | 
(29) 
MSE = 1 
L 
L 
 
i =1 
(y i −ˆ 
y i ) 2 
(30) 
wher e TP r epr esents the number of corr ectl y identified normal 
samples, TN r epr esents the number of corr ectl y identified abnor- 
mal samples, FP r epr esents the number of normal samples in- 
corr ectl y identified as abnormal, and FN r epr esents the number 
of abnormal samples incorr ectl y identified as normal. L denotes 
the length of each parameter, y i represents the i th data point of 
the original value without anomaly, and ˆ 
y i represents the i th data 
point of the estimated value. 
4.4.2. Baseline methods 
To verify the effectiveness of CA-1DCL-EF, a comparison is con- 
ducted with the state-of-the-art r egr ession methods based on 
LSTM-RF (Wang et al., 2019 ) and STC-LSTM (Zhong et al ., 2022 ). 
In addition, for a compr ehensiv e baseline comparison, KNN and 
support v ector r egr ession (SVR) methods ar e also included. Brief 
descriptions of LSTM-RF, STC-LSTM, KNN, and SVR ar e pr ovided 
as follows: 
(i) LSTM-RF and STC-LSTM: STC-LSTM and LSTM-RF are 
based on LSTM for modeling UAV flight data and ac hie v e 
anomaly detection by comparing the pr ediction err ors with 
the anomaly detection threshold. Unlike STC-LSTM, LSTM- 
RF applies additional smoothing to the prediction errors. 
The network arc hitectur e of STC-LSTM consists of three 
LSTM layers and two fully connected la yers . T he structure 
of LSTM-RF consists of an input layer, an LSTM layer, and 
an output layer. 
(ii) KNN: KNN assesses the degree of anomaly by calculat- 
ing the distance or density of each data point to its KNNs. 
Anomalies are usually considered to be points that are far- 
ther or sparser r elativ e to their neighbors . T he predicted 
Figur e 10: T he violin plots of T hor Flight 98 and T hor Flight 104 datasets . 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 10

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 185 
Figur e 11: T he anomal y detection r esults of C A-1DCL-EF for the bias and drift anomalies . 
output values of the test samples are obtained by averag- 
ing or weighting the output values of these k samples. In 
this paper the value of k is taken as 50. 
(iii) SVR: SVR predicts the values at the next moment by learn- 
ing the features and patterns of the data. Anomalies are 
then identified by comparing the difference between the 
actual observed and predicted values. SVR can utilize var- 
ious kernel functions, such as linear, polynomial, or radial 
basis functions, to learn the high-dimensional feature rep- 
resentation of the data. The kernel function in the SVR 
model in this paper is the radial basis function. 
For the baseline methods, the models have an input size of n 
and an output size of 1, where n represents the number of param- 
eters with correlation. In this study, n is 16. 
4.4.3. Experimental results on Thor Flight 98 dataset 
Anomaly detection 
The anomaly detection visualization results of CA-1DCL-EF for 
the bias and drift anomalies are presented in Fig. 11 . In Fig. 11 a 
and b, the blac k, r ed, and or ange curv es r epr esent the original er- 
r ors, smoothed err ors, and the anomaly determination threshold, 
r espectiv el y. Figur e 11 c and d depict the detected normal data 
and anomalies, r espectiv el y, with the blue and dark r ed curv es. 
The original bias and drift anomaly errors are smoothed using 
EWMA, effectiv el y r educing the false detection rate for both nor- 
mal and abnormal data points, as indicated by the green circles 
in Fig. 11 a and b. Although there are some missed and false de- 
tections, as shown by the blue circles in Fig. 11 c and d, most data 
points are correctly detected. Specifically, CA-1DCL-EF correctly 
identifies 1522 normal and 1596 abnormal samples for the bias 
anomaly and 1496 normal and 1595 abnormal samples for the 
drift anomaly. 
Table 3 lists the ACC, TPR, and FPR values of the baseline meth- 
ods and CA-1DCL-EF. Although SVR corr ectl y detects all the bias 
and drift anomaly samples with FPR values of 0.00%, its TPR val- 
ues are relatively low for the bias and drift anomalies at 62.88% 
and 63.38%, r espectiv el y. T his ma y be due to the r elativ el y weak 
performance of SVR when dealing with complex, nonlinear re- 
lationships or noisy data. The ov er all anomal y detection perfor- 
mance of KNN is poor because of factors such as the selection 
Table 3: Anomal y detection r esults of eac h method for the bias 
and drift anomalies. 
Anomaly type Methods 
ACC 
TPR 
FPR 
Bias anomaly CA-1DCL-EF 
97.44% 
95.13% 
0.25% 
KNN 
74.19% 
77.25% 
28.88% 
SVR 
81.44% 
62.88% 
0.00% 
STC-LSTM 
84.22% 
89.88% 
21.44% 
LSTM-RF 
93.34% 
86.69% 
0.00% 
Drift anomaly CA-1DCL-EF 
96.59% 
93.50% 
0.33% 
KNN 
78.06% 
77.25% 
21.13% 
SVR 
81.69% 
63.38% 
0.00% 
STC-LSTM 
89.03% 
83.44% 
5.68% 
LSTM-RF 
93.72% 
87.44% 
0.00% 
of the k value and high data dimensionality, especially in terms 
of FPR values for the bias and drift anomalies, up to 28.88% and 
21.13%, r espectiv el y. LSTM-RF and STC-LSTM perform r elativ el y 
well compared with SVR and KNN, which is mainly because LSTM 
can effectiv el y ca ptur e the long-term dependencies in flight data. 
The ACC and TPR values of LSTM-RF and STC-LSTM ar e mor e than 
84.00% and 83.00%, r espectiv el y. Although the FPR v alues of CA- 
1DCL-EF are lo w er than those of SVR and LSTM-RF, CA-1DCL-EF 
ac hie v es the highest ACC and TPR values with 97.44% and 95.13% 
for the bias anomaly, and 96.59% and 93.50% for the drift anomaly, 
r espectiv el y. 
To further illustrate the adv anta ges of the proposed method, 
Table 4 presents the difference values of each performance met- 
ric between CA-1DCL-EF and the baseline methods, which can be 
calculated by 	υ = 	υour −	υme , where 	 indicates the value of 
the difference, υ denotes the anomaly detection evaluation met- 
rics and υ ∈ [ACC, TPR, FPR], our denotes CA-1DCL-EF, and me in- 
dicates the methods mentioned above and me ∈ [SVR, KNN, STC- 
LSTM, LSTM-RF]. “+ ” indicates an increase and “−” indicates a de- 
crease. It can be observed that the differences in ACC and TPR val- 
ues between CA-1DCL-EF and the baseline methods are all posi- 
tiv e, with r espectiv e r anges of v ariation being 2.87% to 23.25% and 
5.25% to 32.25%. Although CA-1DCL-EF exhibits lo w er TPR values 
compared with SVR and LSTM-RF, as mentioned earlier, the differ- 
ences are relatively small, with bias and drift anomalies of only 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 11

186 | UAV flight data anomaly detection and recovery 
Ta ble 4: The differences betw een CA-1DCL-EF and the baseline 
methods. 
Anomaly type Method 
ACC 
TPR 
FPR 
Bias anomaly KNN 
+ 23.25% 
+ 17.88% 
−28.63% 
SVR 
+ 16.00% 
+ 32.25% 
+ 0.25% 
STC-LSTM 
+ 13.22% 
+ 5.25% 
−21.19% 
LSTM-RF 
+ 4.10% 
+ 8.44% 
+ 0.25% 
Drift anomaly KNN 
+ 18.53% 
+ 16.25% 
−20.80% 
SVR 
+ 14.90% 
+ 30.12% 
+ 0.33% 
STC-LSTM 
+ 7.56% 
+ 10.06% 
−5.35% 
LSTM-RF 
+ 2.87% 
+ 6.06% 
+ 0.33% 
0.25% and 0.33%, r espectiv el y. In contr ast, the differ ences in the 
FPR values of KNN and STC-LSTM versus CA-1DCL-EF ar e mor e 
significantly higher at −28.63% and −21.19%, and −20.80% and 
−5.35% for the bias and drift anomalies, r espectiv el y. The r esults 
show that CA-1DCL-EF can significantl y impr ov e in most metrics 
compared with the benchmark methods, verifying the effective- 
ness of CA-1DCL-EF in detecting different anomaly types. 
Da ta reco very 
Figur e 12 illustr ates the visualization of data r ecov ery r esults 
for CA-1DCL-EF, KNN, SVR, STC-LSTM, and LSTM-RF, where the 
black and red curves represent the original and estimated data, 
r espectiv el y. KNN and SVR show mor e pr onounced r ecov ery bi- 
ases in some local regions, as sho wn b y the orange and blue cir- 
cles in Fig. 12 . This may be due to the sensitivity of KNN to noise 
or local fluctuations and the lack of flexibility in SVR to capture 
certain complex nonlinear r elationships, r esulting in mor e pr o- 
nounced r estor ation biases in some local r egions. In contr ast, the 
Table 5: Data r ecov ery r esults of the abov e methods. 
Anomaly type 
Method 
MAE 
MSE 
Bias anomaly 
CA-1DCL-EF 
0.04 107 
0.00 214 
KNN 
0.09682 
0.01641 
SVR 
0.04184 
0.00278 
STC-LSTM 
0.04638 
0.00333 
LSTM-RF 
0.04744 
0.00384 
Drift anomaly 
CA-1DCL-EF 
0.04441 
0.00 239 
KNN 
0.09682 
0.01641 
SVR 
0.03 805 
0.00245 
STC-LSTM 
0.04632 
0.00343 
LSTM-RF 
0.04935 
0.00417 
predictions of CA-1DCL-EF, STC-LSTM, and LSTM-RF do not show 
any significant biases o verall. T his suggests that these methods 
ar e mor e successful in capturing the nonlinear relationships and 
patterns within the data. 
Table 5 lists the MAE and MSE values of the r egr ession perfor- 
mance metrics for the above methods. KNN exhibits the highest 
MAE and MSE values, with 0.09 682 and 0.01 641, r espectiv el y, for 
the bias and drift anomalies. SVR, STC-LSTM, LSTM-RF, and CA- 
1DCL-EF present lo w er MAE and MSE values for the bias and drift 
anomalies. Specifically, for the drift anomaly, CA-1DCL-EF has an 
MAE v alue of 0.04 441, whic h is slightl y lo w er than that of SVR, 
but compared with SVR, STC-LSTM, and LSTM-RF, it achieves the 
lo w est MSE value of 0.00 239. Particularly for the bias anomaly, CA- 
1DCL-EF exhibits the lo w est MAE and MSE values of 0.04 107 and 
0.00 214, r espectiv el y, compar ed with the baseline methods. In ad- 
dition, it is observed that for the drift anomaly, the MAE and MSE 
Figure 12: Data r ecov ery visualization of the above methods. 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 12

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 187 
Figur e 13: T he anomal y detection r esults of C A-1DCL-EF for the bias and drift anomalies . 
Table 6: Anomal y detection r esults of eac h method for the bias 
and drift anomalies. 
Anomaly type 
Methods 
ACC 
TPR 
FPR 
Bias anomaly 
CA-1DCL-EF 
91.53% 
87.50% 
4.44% 
KNN 
64.59% 
57.88% 
30.94% 
SVR 
65.09% 
57.19% 
27.00% 
STC-LSTM 
85.41% 
78.25% 
7.44% 
LSTM-RF 
81.50% 
70.50% 
7.50% 
Drift anomaly 
CA-1DCL-EF 
94.22% 
88.44% 
0.00% 
KNN 
69.25% 
57.88% 
19.38% 
SVR 
71.31% 
57.31% 
14.69% 
STC-LSTM 
87.34% 
83.06% 
8.38% 
LSTM-RF 
80.31% 
60.63% 
0.00% 
values of the above methods are generally higher than those of 
the bias anomaly. T his ma y be due to the greater degree of injected 
drift anomaly than the bias anomal y, whic h makes the data devi- 
ate mor e significantl y fr om the norm, thus triggering more signifi- 
cant uncertainty and volatility. With this uncertainty, the model’s 
data r ecov ery ability may be mor e c hallenged, leading to r elativ el y 
high MAE and MSE v alues. Ne v ertheless, the ov er all data r ecov ery 
performance of CA-1DCL-EF is still significantly better than that 
of the other compared methods, further validating its effective- 
ness in data r ecov ery. 
4.4.4. Experimental results on Thor Flight 104 dataset 
Anomaly detection 
Figure 13 shows the results of the anomaly detection visual- 
ization of CA-1DCL-EF for the bias and drift anomalies. It can be 
seen that using EWMA for error smoothing still significantly re- 
duces the false detection rate of certain points with drastic error 
variations, as shown by the green circles in Fig. 13 . Howe v er, it 
is undeniable that CA-1DCL-EF appears to have a relatively high 
number of missed or false detections, as shown by the black cir- 
cles in Fig. 13 . 
Table 6 lists the anomaly detection performance metrics for the 
abo ve methods . It can be clearl y observ ed that CA-1DCL-EF sig- 
nificantly outperforms the other compared methods in bias and 
drift anomal y detection. Specificall y, the ACC, TPR, and FPR v al- 
Ta ble 7: The differences betw een CA-1DCL-EF and the baseline 
methods. 
Anomaly type 
Method 
ACC 
TPR 
FPR 
Bias anomaly 
KNN 
+ 26.94% 
+ 29.62% 
−26.50% 
SVR 
+ 26.44% 
+ 30.30% 
−22.56% 
STC-LSTM 
+ 6.12% 
+ 9.25% 
−3.00% 
LSTM-RF 
+ 10.03% 
+ 17.00% 
−3.06% 
Drift anomaly 
KNN 
+ 24.97% 
+ 30.56% 
−19.38% 
SVR 
+ 22.91% 
+ 31.13% 
−14.69% 
STC-LSTM 
+ 6.88% 
+ 5.38% 
−8.38% 
LSTM-RF 
+ 13.91% 
+ 27.81% 
+ 0.00% 
ues for CA-1DCL-EF are 91.53%, 87.50%, and 4.44% for the bias 
anomaly, and 94.22%, 88.44%, and 0.00% for the drift anomal y, r e- 
spectiv el y. T he o v er all performances of KNN and SVR in anomaly 
detection ar e r elativ el y poor, especiall y with high FPR v alues of 
30.94% and 27.00%, and 19.38% and 14.69% for the bias and drift 
anomalies, r espectiv el y. In contr ast, STC-LSTM and LSTM-RF ex- 
hibit r elativ el y lo w er FPR values of 7.44% and 7.50%, and 8.38% 
and 0.00%, for the bias and drift anomalies, r espectiv el y. Ho w e v er, 
STC-LSTM and LSTM-RF still perform r elativ el y poorl y in terms of 
ACC and TPR values. 
Similarl y, to pr ovide mor e insight into the adv anta ges of the 
proposed method, the difference values of the performance met- 
rics between CA-1DCL-EF and the baseline methods are demon- 
strated in Table 7 . As described pr e viousl y, the ov er all anomal y de- 
tection performances of KNN and SVR are relatively poor, which 
can also be reflected in their 	ACC, 	TPR, and 	FPR values. For 
example, for the bias and drift anomalies, the ACC and TPR val- 
ues of CA-1DCL-EF are higher than those of KNN by 26.94% and 
29.62%, and 24.97% and 30.56%, r espectiv el y. The FPR v alues of 
KNN are 26.50% and 19.38% higher than those of CA-1DCL-EF, 
r espectiv el y, for the bias and drift anomalies. For the bias and 
drift anomalies, the differences between SVR and CA-1DCL-EF 
also show a similar trend to KNN. Compared with KNN and SVR, 
although the performance differences between STC-LSTM and 
LSTM-RF versus CA-1DCL-EF are reduced, the magnitude of the 
differ ence c hange is still r elativ el y high for most performance 
metrics. 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 13

188 | UAV flight data anomaly detection and recovery 
Figure 14: Data r ecov ery visualization of the above methods. 
Table 8: Data r ecov ery r esults of the abov e methods. 
Anomaly type 
Method 
MAE 
MSE 
Bias anomaly 
CA-1DCL-EF 
0.03 574 
0.00 183 
KNN 
0.06126 
0.00711 
SVR 
0.05506 
0.00483 
STC-LSTM 
0.04061 
0.00251 
LSTM-RF 
0.03961 
0.00222 
Drift anomaly 
CA-1DCL-EF 
0.04 049 
0.00 226 
KNN 
0.06126 
0.00711 
SVR 
0.05526 
0.00487 
STC-LSTM 
0.04158 
0.00260 
LSTM-RF 
0.04211 
0.00250 
Da ta reco very 
Figure 14 shows the visualization of data recovery results for 
the abo ve methods . It can be clearly seen that KNN and SVR are 
still unable to accur atel y pr edict some local r egion data points 
w ell, as sho wn b y the orange and blue cir cles in Fig. 14 , for the 
r easons mentioned earlier. Compar ed with KNN and SVR, LSTM- 
RF, STC-LSTM, and CA-1DCL-EF do not exhibit more significant 
r ecov ery biases in predicting different anomaly types of data. 
Table 8 lists the MAE and MSE values for the above methods. 
For the baseline methods, KNN and SVR show significantly higher 
MAE and MSE values for the bias and drift anomalies than STC- 
LSTM, and LSTM-RF. Taking the bias anomaly as an example, the 
MAE and MSE values of STC-LSTM and LSTM-RF are 0.04 061 and 
0.00 251, and 0.03 961 and 0.00 222, r espectiv el y, wher eas those of 
KNN and SVR are 0.06 126 and 0.00 711, and 0.05 506 and 0.00 483 
r espectiv el y. Compar ed with the baseline methods , C A-1DCL-EF 
ac hie v es the optimal data r ecov ery performance, i.e., the small- 
Table 9: Anomaly detection results of LSTM and 1D CNN. 
Dataset name 
Anomaly type Method 
ACC 
TPR 
FPR 
Thor Flight 98 
Bias anomaly LSTM 
80.22% 60.44% 0.00% 
1D CNN 
87.69% 85.56% 10.19% 
Drift anomaly LSTM 
79.72% 59.44% 0.00% 
1D CNN 
92.66% 85.69% 
0.38% 
Thor Flight 104 
Bias anomaly LSTM 
89.81% 89.81% 10.19% 
1D CNN 
67.16% 38.06% 
3.75% 
Drift anomaly LSTM 
93.84% 90.00% 2.31% 
1D CNN 
68.96% 37.94% 0.00% 
est MAE and MSE values of 0.03 574 and 0.00 183, and 0.04 049 
and 0.00 226, r espectiv el y, for the bias and drift anomalies. Sim- 
ilarly, the MAE and MSE values of the above methods for the drift 
anomal y ar e gener all y higher than those for the bias anomaly, 
which is due to the reasons mentioned previously. 
Ablation study 
T his subsection in v estigates the anomal y detection and data 
r ecov ery performance of LSTM and 1D CNN as ablation experi- 
ments on different flight datasets . T he anomaly detection perfor- 
mance metrics of LSTM and 1D CNN on different datasets are 
given in Table 9 . It can be seen that LSTM can detect all the 
bias and drift anomaly samples of the Thor Flight 98 dataset, 
i.e., all the FPR values are 0.00%, but its ACC and TPR values 
ar e r elativ el y lo w. 1D CNN sho ws r elativ el y good anomal y de- 
tection performance on the Thor Flight 98 dataset, with its ACC 
and TPR values exceeding 87.00% and 85.00% for the bias and 
drift anomalies, r espectiv el y. In contr ast, for the Thor Flight 104 
dataset, LSTM performs better in terms of TPR v alues, e v en ex- 
ceeding CA-1DCL-EF, for the bias and drift anomalies of 89.81% 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 14

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 189 
Figure 15: Data r ecov ery visualization of LSTM and 1D CNN. 
Table 10: Data r ecov ery r esults of LSTM and 1D CNN. 
Dataset name 
Anomaly type 
Method 
MAE 
MSE 
Thor Flight 98 
Bias anomaly 
LSTM 
0.04 096 
0.00 223 
1D CNN 
0.07214 
0.00736 
Drift anomaly 
LSTM 
0.04 161 
0.00 227 
1D CNN 
0.07202 
0.00756 
Thor Flight 104 
Bias anomaly 
LSTM 
0.03834 
0.00205 
1D CNN 
0.04355 
0.00304 
Drift anomaly 
LSTM 
0.04151 
0.00237 
1D CNN 
0.04449 
0.00320 
and 90.00%, r espectiv el y, but still shows high FPR values of 10.19% 
and 2.31%, r espectiv el y. Although 1D CNN maintains low FPR 
values on the Thor Flight 104 dataset, its ACC and TPR values 
perform unsatisfactorily. This phenomenon may be due to the 
difference in data distribution between different datasets. Al- 
though LSTM and 1D CNN have their own advantages and dis- 
adv anta ges on differ ent datasets , they ha v e a syner gistic effect 
in reducing the FPR values or improving the ACC and TPR val- 
ues . T his synergy allows CA-1DCL-EF to ac hie v e a better balance 
in anomaly detection performance and provide a mor e r eliable 
solution. 
Figure 15 shows the recovery visualization of LSTM and 1D CNN 
on different flight datasets. It can be clearly seen that LSTM and 
1D CNN show some r ecov ery biases on different flight datasets, 
as shown by the red and black circles in Fig. 15 . To quantify the 
r ecov ery performance of LSTM and 1D CNN, Table 10 lists their 
MAE and MSE v alues on differ ent flight datasets. An obvious phe- 
nomenon is that the MAE and MSE of 1D CNN are generally higher 
than those of LSTM for different flight datasets, which can also 
be seen from the red circles in Fig. 15 . For example, for the bias 
and drift anomalies of the Thor Flight 104 dataset, the MAE and 
MSE values of 1D CNN are 0.04 355 and 0.00 304, and 0.04 449 and 
0.00 320, whereas those of LSTM are 0.03 834 and 0.00 205, and 
0.04 151 and 0.00 237, r espectiv el y. The differ ence in performance 
between LSTM and 1D CNN may be due to the temporal nature 
of the flight data, whereas LSTM is more advantageous relative to 
1D CNN in processing this type of data. Meanwhile, it is observed 
that the MAE and MSE values of the bias anomaly are generally 
lo w er than the drift anomaly for 1D CNN and LSTM on all flight 
datasets, for the reasons described previously. In addition, for the 
Thor Flight 98 dataset, LSTM outperforms CA-1DCL-EF with MAE 
and MSE values of 0.04 096 and 0.00 223, and 0.04 161 and 0.00 227, 
r espectiv el y, for the bias and drift anomalies. Ho w e v er, LSTM fo- 
cuses on long-term dependency modeling and cannot accur atel y 
predict local regions with sharp changes, as sho wn b y the black 
circles in Fig. 15 . This leads to more false detections. As men- 
tioned earlier, LSTM has r elativ el y low TPR v alues despite being 
able to corr ectl y detect all anomalous samples in the Thor Flight 
98 dataset. 
4.4.5. Effects of parameter selection and EF 
To assess the impact of the input parameter number and EF on 
the model’s performance, Table 11 presents the anomaly detec- 
tion results of 1DCL-EF and CA-1DCL on different flight datasets. 
1DCL-EF r epr esents the model without parameter selection and 
CA-1DCL denotes the model without EF. It can be seen that CA- 
1DCL has r elativ el y good anomal y detection performance on dif- 
ferent flight datasets. For the bias and drift anomalies of the Thor 
Flight 98 dataset, the ACC, TPR, and FPR values of CA-1DCL are 
96.13%, 94.44%, and 2.19%, and 96.38%, 92.75%, and 0.06%, respec- 
tiv el y. It is note worthy that the FPR v alue of CA-1DCL for the drift 
anomaly is better than that of C A-1DCL-EF. T his is because EWMA 
is not sensitive to rapid changes in data and is more concerned 
with the ov er all tr end, whic h may lead to abnormal starting posi- 
tion data being incorr ectl y judged as normal data, as shown by the 
red circles in Figs. 11 a and b. This is not always the case, ho w e v er, 
and is related to the threshold and errors. Although for the Thor 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 15

190 | UAV flight data anomaly detection and recovery 
Table 11: Anomaly detection results of CA-1DCL and 1DCL-EF. 
Dataset name 
Anomaly type 
Method 
ACC 
TPR 
FPR 
Thor Flight 98 
Bias anomaly 
CA-1DCL 
96.13% 
94.44% 
2.19% 
1DCL-EF 
84.84% 
83.19% 
13.50% 
Drift anomaly 
CA-1DCL 
96.38% 
92.75% 
0.06% 
1DCL-EF 
80.53% 
70.06% 
7.13% 
Thor Flight 104 
Bias anomaly 
CA-1DCL 
88.06% 
85.63% 
9.50% 
1DCL-EF 
88.28% 
86.88% 
10.31% 
Drift anomaly 
CA-1DCL 
90.94% 
85.57% 
3.69% 
1DCL-EF 
85.69% 
71.38% 
0.00% 
Table 12: Anomaly detection results of PCC-1DCL-EF. 
Dataset name 
Anomaly type 
ACC 
TPR 
FPR 
Thor Flight 98 
Bias anomaly 
94.56% 
90.56% 
1.44% 
Drift anomaly 
94.25% 
88.63% 
0.13% 
Thor Flight 104 
Bias anomaly 
80.19% 
62.50% 
2.13% 
Drift anomaly 
79.19% 
58.94% 
0.56% 
Flight 98 dataset, the difference in performance between CA-1DCL 
and CA-1DCL-EF is r elativ el y small, ho w e v er, for the Thor Flight 
104 dataset, the adv anta ge of err or smoothing is m uc h mor e pr o- 
nounced, especially in reducing the FPR values. 
For 1DCL-EF, its ov er all anomal y detection performance on 
different flight datasets is relatively poor. For the bias and drift 
anomalies of the Thor Flight 98 dataset, the ACC, TPR, and FPR 
values for 1DCL-EF are 84.84%, 83.19%, and 13.50%, and 80.53%, 
70.06%, and 7.13%, r espectiv el y. For the Thor Flight 104 dataset, 
although 1DCL-EF ac hie v es an FPR v alue of 0.00% for the drift 
anomaly, it still performs relatively poorly for ACC and TPR values 
and in the bias anomaly detection. This may be due to too many 
input par ameters, r esulting in an underfitting of 1DCL-EF. In con- 
tr ast, CA-1DCL-EF impr ov es the anomaly detection performance 
by effectiv el y ov ercoming the underfitting pr oblem thr ough pa- 
rameter selection. 
4.4.6. Model performance of PCC-based parameter selection 
To further explore the advantage of MIC-based parameter selec- 
tion, Table 12 shows the anomaly detection results of the method 
using PCC for parameter selection, named PCC-1DCL-EF, on dif- 
ferent flight datasets. PCC-1DCL-EF performs well on the Thor 
Flight 98 dataset, with ACC, TPR, and FPR values of 94.56%, 90.56%, 
and 1.44%, and 94.25%, 88.63%, and 0.13% for the bias and drift 
anomalies, r espectiv el y. Ho w e v er, for the Thor Flight 104 dataset, 
it suffers from a more pronounced false detection problem, with 
TPR v alues of onl y 62.50% and 58.94% for the bias and drift 
anomalies, r espectiv el y. Although PCC-1DCL-EF has r elativ el y low 
FPR values, in some cases even lo w er than CA-1DCL-EF, its over- 
all performance is still inferior to C A-1DCL-EF. T his difference is 
especially significant on the Thor Flight 104 dataset. The reasons 
for the r elativ el y significant differ ence in the performance of PCC- 
1DCL-EF on different flight datasets may be attributed to multiple 
factors, such as differences in data distribution and the loss of k e y 
nonlinear parameters that positively impact model performance. 
Figure 16 shows the data recovery visualization of PCC-1DCL- 
EF on different flight datasets. It can be seen that PCC-1DCL- 
EF does not show significant r ecov ery biases on different flight 
datasets. Table 13 quantifies the r ecov ery performance metrics 
of PCC-1DCL-EF on different flight datasets. It can be clearly ob- 
served that the MAE values of PCC-1DCL-EF are lo w er than those 
of CA-1DCL-EF for different flight datasets, while the MSE values 
are higher than those of C A-1DCL-EF. T his is due to the fact that 
the MIC-based parameter selection contains many nonlinear cor- 
r elation par ameters whic h may lead to lar ge absolute err ors on 
some samples, making the MAE values relatively high. T herefore , 
compared with PCC-1DCL-EF, CA-1DCL-EF achieves a better trade- 
off between anomaly detection and data recovery performance by 
taking into account the nonlinear correlation parameters in the 
flight data. 
4.4.7. Discussion 
This subsection discusses the r esearc h r esults on solving the prob- 
lems of r andom noise, par ameter selection, and featur e extr action 
using the pr oposed fr ame work CA-1DCL-EF and giv es the follow- 
ing main findings: 
First, compared with the baseline methods , C A-1DCL-EF 
ac hie v es excellent anomaly detection performance on different 
flight datasets with the highest TPR and ACC values while main- 
taining lo w er FPR v alues. Furthermor e, CA-1DCL-EF also exhibits 
superior r ecov ery performance on differ ent flight datasets, whic h 
can be reflected by its lo w er MAE and MSE values . T hese results 
demonstrate that CA-1DCL-EF has good generalization and ro- 
bustness , pro viding an effective and practical solution to ensure 
the safe flight of UAVs and their intelligent operation and main- 
tenance. 
Second, the ablation experiments conducted in this study pro- 
vide valuable insights into the individual contributions of 1D CNN 
and LSTM in anomaly detection and data recovery tasks . T he re- 
sults r e v eal that using 1D CNN or LSTM alone yielded r elativ el y 
poor tempor al featur e modeling or local featur e extr action per- 
formance. Ho w e v er, integr ating these two a ppr oac hes in the de- 
signed 1D CNN-LSTM model synergizes their strengths and bet- 
ter balances data r ecov ery and anomaly detection performance. 
This finding highlights the importance of utilizing hybrid models 
that le v er a ge m ultiple deep-learning arc hitectur es to handle the 
complex nature of sequential data effectively. 
Thir d, b y utilizing the feature extraction capability of 1D CNN- 
LSTM model and combining the EWMA and MIC methods to deal 
with noise and ca ptur e complex spatio-tempor al corr elation, the 
anomaly detection and data recovery impacts of CA-1DCL-EF are 
impr ov ed mor e significantl y. This integr ated a ppr oac h pr ovides a 
v aluable r efer ence for the pr actical a pplication of accur ate and r e- 
liable UAV anomaly detection and data r ecov ery. Meanwhile, the 
ov er all better performance of anomaly detection and data recov- 
ery based on MIC parameter selection compared with PCC pro- 
vides important guidance for future research and applications. 
Although this study r e v eals some important findings, some 
limitations must be acknowledged. First, UAV flight data may be 
affected by m ultiple factors, r esulting in different types and de- 
gr ees of anomalies. Manuall y injected anomal y data ar e often 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 16

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 191 
Figure 16: Data r ecov ery visualization of PCC-1DCL-EF. 
Table 13: Data r ecov ery r esults of PCC-1DCL-EF. 
Dataset name 
Anomaly type 
MAE 
MSE 
Thor Flight 98 
Bias anomaly 
0.03 867 
0.00254 
Drift anomaly 
0.04 106 
0.00284 
Thor Flight 104 
Bias anomaly 
0.03 520 
0.00199 
Drift anomaly 
0.03 804 
0.00228 
pre-defined fixed patterns that cannot full y sim ulate the complex 
anomaly types in actual UAV flight data. Second, given the limita- 
tions of the data emplo y ed in this paper, the assessment of noise’s 
impact on anomaly detection performance remains incomplete. 
Third, the threshold setting in this paper is calculated using a sta- 
tistical method and is static. It cannot be ada ptiv el y adjusted ac- 
cording to the dynamic changes of UAV flight data, which may 
lead to more false alarms or missed alarms. Finally, although this 
paper uses the advanced methods in the field as the comparison 
methods, they are not sufficient. 
Ther efor e, futur e r esearc h can focus on the following aspects 
to address the aforementioned limitations: (i) Incorporating more 
compr ehensiv e anomal y types, suc h as stuc k anomal y and com- 
pound anomaly (Y. He et al., 2018 ; Zhong et al ., 2022 ), into future 
experiments to impr ov e the r epr esentativ eness and persuasive- 
ness of the experiments. (ii) Introducing different noise levels to 
assess their impact on the accuracy and stability of the model. (iii) 
Combining ada ptiv e methods (Fang et al., 2022 ; Hou et al., 2023 ) for 
anomaly detection to reduce the false alarm rate and enhance the 
generalization performance of the model. (iv) Including more ad- 
v anced anomal y detection methods for time-series data into the 
study, such as TimesNet (Wu et al., 2022 ), to fully evaluate the ef- 
fectiveness of the model. 
5. Conclusions 
To ac hie v e accur ate anomal y detection and r eliable data r ecov- 
ery in UAV flight data, this paper proposed a novel comprehen- 
siv e fr ame work named CA-1DCL-EF. First, the MIC-based method 
is used to select correlation parameters as model input to avoid 
the negative influence of unrelated variables on the model. Sec- 
ond, a r egr ession model based on 1D CNN-LSTM was designed 
to compr ehensiv el y ca ptur e the spatio-tempor al featur es in the 
flight data and realize more accurate parameter mapping. Then, 
the err ors wer e smoothed by the EWMA method to r educe the im- 
pact of random noise on the model performance. Finally, experi- 
ments were performed on real UAV flight datasets injected with 
bias and drift anomalies . T he anomaly detection and data recov- 
ery results on different flight datasets demonstrated that the over- 
all performance of CA-1DCL-EF was significantly better than the 
baseline methods. In addition, the necessity and effectiveness of 
parameter selection and error smoothing on model performance 
impr ov ement wer e v erified, offering r efer ence v alue for UAV flight 
data anomaly detection and recovery. 
In the future, the effective integration of various methods will 
be continuously optimized and explored for practical problems to 
further impr ov e the anomal y detection performance of the model. 
Meanwhile, differ ent anomal y types, noise le v els, and other ad- 
vanced methods will also be included in futur e r esearc h and ex- 
periments to further verify the generality and effectiveness of the 
proposed method. In addition, research will be conducted on the 
ada ptiv e detection pr oblem to de v elop methods that can dynam- 
ically adjust the anomaly detection thresholds, thereby reducing 
the false alarm rate. 
Ac kno wledgments 
The authors would like to thank the National Natural Science 
Foundation of China (No.52275480) and the National K ey R&D Pr o- 
gram of China (No.2020YFB1713300) for providing support for this 
pa per. Especiall y thanks for the computing support of the State 
K ey Labor atory of Public Big Data, Guizhou Univ ersity. 
Conflict of interest statement 
None declared. 
References 
Abbaspour , A., Aboutalebi, P., Yen, K. K., & Sargolzaei, A. (2017). Neu- 
r al ada ptiv e observ er-based sensor and actuator fault detection 
in nonlinear systems: Application in UA V. ISA T ransactions , 67 , 
317–329. https:// doi.org/ 10.1016/ j.isatra.2016.11.005 .
Ahmad , M. W., Akram, M. U., Ahmad, R., Hameed, K., & Hassan, 
A. (2022). Intelligent fr ame work for automated failur e pr edic- 
tion, detection, and classification of mission critical autonomous 
flights. ISA Transactions , 129 , 355–371. https:// doi.org/ 10.1016/ j.is 
atra.2022.01.014 .
Alos , A. M., Dahrouj, Z., & Dakkak, M. (2020). A nov el tec hnique to 
assess UAV behavior using PCA-based anomaly detection algo- 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 17

192 | UAV flight data anomaly detection and recovery 
rithm. International Journal of Mechanical Engineering and Robotics Re- 
search , 9 , 721–726. https:// doi.org/ 10.18178/ijmerr.9.5.721-726 .
Alos , A., & Dahrouj, Z. (2020). Detecting contextual faults in un- 
manned aerial vehicles using dynamic linear regression and k- 
nearest neighbour classifier. Gyroscopy and Navigation , 11 , 94–104. 
https:// doi.org/ 10.1134/ S2075108720010046 .
Bae , G . , & J oe , I. (2020). UAV anomaly detection with distributed ar- 
tificial intelligence based on LSTM-AE and AE. In Park J ., Y ang L., 
Jeong Y. S., & Hao F. (Eds.), Advanced multimedia and ubiquitous en- 
gineering. MUE FutureTech 2019 2019. Lecture notes in electrical engi- 
neering (Vol. 590 , pp. 305–310). Springer. https:// doi.org/ 10.1007/ 97 
8- 981- 32- 9244- 4 _ 43 .
Bronz , M., Baskaya, E., Delaha ye , D., & Puec hmor e, S. (2020). Real-time 
fault detection on small fixed-wing UAVs using machine learning. 
In Proceedings of the 2020 AIAA/IEEE 39th Digital Avionics Systems 
Conference (DASC) (pp. 1–10). IEEE. https:// doi.org/ 10.1109/ DASC50 
938.2020.9256800 .
Bu , J. , Sun, R. , Bai, H. , Xu, R. , Xie, F. , Zhang, Y. , & Ochieng, W .Y .. (2017) 
Integrated method for the UAV navigation sensor anomaly detec- 
tion, IET Radar Sonar Navig , 11 , 847–853.
Chen , S., Chen, B., Shu, P., Wang, Z., & Chen, C. (2022). Real- 
time unmanned aerial vehicle flight path prediction using a bi- 
directional long short-term memory network with error compen- 
sation. Journal of Computational Design and Engineering , 10 (1), 16–35. 
https:// doi.org/ 10.1093/ jcde/qwac125 .
Duan , Y. , Zhao , Y. , Xu, Y. , Peng, Y. , & Liu, D. (2017). Unmanned aerial 
vehicle sensor data anomaly detection using kernel principle 
component analysis. In Proceedings of the 2017 13th IEEE Interna- 
tional Conference on Electronic Measurement & Instruments (ICEMI) (pp. 
241–246). IEEE. https:// doi.org/ 10.1109/ ICEMI.2017.8265777 .
F ang , Z. , Wang, J. , Ren, Y. , Han, Z. , Poor, H. V. , & Hanzo , L. (2022). Age of 
information in energy harvesting aided massive multiple access 
networks. IEEE Journal on Selected Areas in Communications , 40 (5), 
1441–1456. https:// doi.org/ 10.1109/ JSA C.2022.3143252 . 
Fr eeman , P., P andita, R., Sriv astav a, N. , & Balas, G . J. (2013). Model- 
based and data-driven fault detection performance for a small 
UA V. IEEE/ASME T ransactions on Mechatronics , 18 (4), 1300–1309. ht 
tps:// doi.org/ 10.1109/ TMECH.2013.2258678 .
Gr av es , A. (2012). Long short-term memory. In Supervised Sequence La- 
belling with Recurrent Neural Networks. Studies in Computational In- 
telligence (Vol. 385 , pp. 37–45). Springer. https:// doi.org/ 10.1007/ 97 
8- 3- 642- 24797- 2 _ 4 .
Gu , J., Wang, B., & Liu, D. (2022). A baseline modeling method for UAV 
condition monitoring based on multiple flight data. In 2022 IEEE 
International Conference on Sensing, Diagnostics , Prognostics , and Con- 
trol (SDPC) (pp. 139–144). IEEE. https:// doi.org/ 10.1109/ SDPC55702. 
2022.9915880 .
He , K., Yu, D ., Wang, D ., Chai, M., Lei, S., & Zhou, C. (2022). Gr a ph at- 
tention network-based fault detection for UAVs with m ultiv ari- 
ant time series flight data. IEEE Transactions on Instrumentation and 
Measurement , 71 , 1–13. https:// doi.org/ 10.1109/ TIM.2022.3219489 .
He , Y ., Peng, Y ., Wang, S., & Liu, D. (2018). ADMOST: UAV flight data 
anomaly detection and mitigation via online subspace tracking. 
IEEE Transactions on Instrumentation and Measurement , 68 (4), 1035–
1044. https:// doi.org/ 10.1109/ TIM.2018.2863499 .
He , Y., Peng, Y., Wang, S., Liu, D., & Leong, P. H. (2017). A structured 
sparse subspace learning algorithm for anomaly detection in UAV 
flight data. IEEE Transactions on Instrumentation and Measurement , 
67 (1), 90–100. https:// doi.org/ 10.1109/ TIM.2017.2754698 .
Hildmann , H., & K o vacs , E. (2019). Using unmanned aerial vehicles 
(UAVs) as mobile sensing platforms (MSPs) for disaster response, 
civil security and public safety. Drones , 3 (3), 59. https:// doi.org/ 10 
.3390/drones3030059 .
Hodson , T. O. (2022). Root-mean-squar e err or (RMSE) or mean abso- 
lute error (MAE): When to use them or not. Geoscientific Model De- 
velopment , 15 (14), 5481–5487. https:// doi.org/ 10.5194/ gmd- 15- 548 
1-2022 .
Hou , X., Wang, J., Jiang, C., Zhang, X., Ren, Y., & Debbah, M. (2023). 
UAV-enabled covert federated learning. IEEE Transactions on Wire- 
less Communications , 22 , 6793. https:// doi.org/ 10.1109/ TWC.2023.3 
245621 .
J ahan , A., & Edw ar ds, K. L. (2015). A state-of-the-art survey on the 
influence of normalization techniques in ranking: Improving the 
materials selection process in engineering design. Materials & De- 
sign (1980-2015) , 65 , 335–342. https:// doi.org/ 10.1016/ j.matdes.2 
014.09.022 .
Jia , M., Raja, A., & Y uan, J . (2023). A hybrid dela y-a war e a ppr oac h to- 
w ar ds UAV flight data anomaly detection. In Proceedings of the 2023 
International Conference on Computing, Networking and Communica- 
tions (ICNC) (pp. 176–180). IEEE. https:// doi.org/ 10.1109/ ICNC5722 
3.2023.10074138 .
Jing , W., & Shimada, K. (2017). Model-based view planning for build- 
ing inspection and surveillance using voxel dilation, medial ob- 
jects, and random-k e y genetic algorithm. Journal of Computational 
Design and Engineering , 5 (3), 337–347. https:// doi.org/ 10.1016/ j.jc 
de.2017.11.013 .
Kir an yaz , S., Avci, O ., Abdeljaber , O ., Ince, T., Gabbouj, M., & Inman, 
D. J. (2021). 1D convolutional neural networks and applications: A 
surv ey. Mec hanical Systems and Signal Processing , 151 , 107398. https: 
// doi.org/ 10.1016/ j.ymssp .2020.107398 . 
Li , C., Li, S., Zhang, A., Yang, L., Zio, E., Pecht, M., & Gryllias, K. (2022). 
A Siamese hybrid neural network framework for few-shot fault 
diagnosis of fixed-wing unmanned aerial vehicles. Journal of Com- 
putational Design and Engineering , 9 (4), 1511–1524. https://doi.org/ 
10.1093/jcde/qwac070 .
Liang , S., Zhang, S. , Huang, Y. , Zheng, X. , Cheng, J. , & Wu, S. (2022). 
Data-driven fault diagnosis of FW-UAVs with consideration of 
m ultiple oper ation conditions. ISA Transactions , 126 , 472–485. ht 
tps:// doi.org/ 10.1016/ j.isatra.2021.07.043 .
Liu , J ., Xiang, J ., Jin, Y., Liu, R., Y an, J ., & Wang, L. (2021). Boost pre- 
cision a gricultur e with unmanned aerial vehicle remote sens- 
ing and edge intelligence: A survey. Remote Sensing , 13 (21), 4387. 
https:// doi.org/ 10.3390/ rs13214387 .
Liu , Y ., & Ding, W . (2015). A KNNS based anomaly detection method 
applied for UAV flight data stream. In Proceedings of the 2015 Prog- 
nostics and System Health Management Conference (PHM) (pp. 1–8). 
IEEE. https:// doi.org/ 10.1109/ PHM.2015.7380051 .
López-Estrada , F. R., Ponsart, J. C., Theilliol, D., Zhang, Y., & Astorga- 
Zar a goza, C. M. (2016). LPV model-based tr ac king contr ol and r o- 
bust sensor fault diagnosis for a quadrotor UAV. Journal of Intel- 
ligent & Robotic Systems , 84 , 163–177. https:// doi.org/ 10.1007/ s108 
46- 015- 0295- y .
Lucas , J. M., & Saccucci, M. S. (1990). Exponentially weighted moving 
av er a ge contr ol sc hemes: Pr operties and enhancements. Tec hno- 
metrics , 32 (1), 1–12. https:// doi.org/ 10.1080/ 00401706.1990.104845 
83 .
Maes , W. H., & Steppe, K. (2019). Perspectives for remote sensing 
with unmanned aerial vehicles in precision agriculture. Trends in 
Plant Science , 24 (2), 152–164. https:// doi.org/ 10.1016/ j.tplants.2018 
.11.007 .
Miao , X., Liu, Y., Zhao, H., & Li, C. (2018). Distributed online one- 
class support vector machine for anomaly detection over net- 
works. IEEE Transactions on Cybernetics , 49 (4), 1475–1488. https: 
// doi.org/ 10.1109/ TCYB.2018.2804940 .
Outay , F., Mengash, H. A., & Adnan, M. (2020). Applications of un- 
manned aerial vehicle (UAV) in road safety, traffic and highway 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026

## Page 18

Journal of Computational Design and Engineering, 2024, 11(2), 176–193 | 193 
infr astructur e mana gement: Recent adv ances and c hallenges. 
Transportation Research Part A: P olic y and Practice , 141 , 116–129. 
https:// doi.org/ 10.1016/ j.tra.2020.09.018 .
Pan , D. (2017). Hybrid data-driv en anomal y detection method to im- 
pr ov e UAV oper ating r eliability. In Proceedings of the 2017 Prognos- 
tics and System Health Management Conference (PHM-Harbin) (pp. 1–
4). IEEE. https:// doi.org/ 10.1109/ PHM.2017.8079281 .
Pan , D., Nie, L., Kang, W., & Song, Z. (2020). UAV anomaly detec- 
tion using active learning and improved S3VM model. In Pro- 
ceedings of the 2020 International Conference on Sensing, Measure- 
ment & Data Analytics in the Era of Artificial Intelligence (ICSMD) 
(pp. 253–258). IEEE. https:// doi.org/ 10.1109/ ICSMD50554.2020.92 
61709 .
Qi , J. , Zhao , X. , Jiang, Z. , & Han, J. (2007). An ada ptiv e thr eshold neur al- 
network scheme for rotorcraft UAV sensor failure diagnosis. In 
Advances in neural networks (pp. 589–596). Springer. https://doi.or 
g/ 10.1007/ 978- 3- 540- 72395- 0 _ 73 .
Qi , X., Theilliol, D., Qi, J., Zhang, Y., & Han, J. (2013). A liter atur e r e- 
view on fault diagnosis methods for manned and unmanned he- 
licopters. In Proceedings of the 2013 International Conference on Un- 
manned Aircraft Systems (ICUAS) (pp. 1114–1118). IEEE. https://doi. 
org/ 10.1109/ ICU AS.2013.6564801 . 
Reshef , D. N. , Reshef , Y. A., Finucane, H. K., Grossman, S. R., McVean, 
G . , Turnbaugh, P. J. , & Sabeti, P. C. (2011). Detecting novel asso- 
ciations in large data sets. Science , 334 (6062), 1518–1524. https: 
// doi.org/ 10.1126/ science.1205438 .
Reshef , D. , Reshef , Y. , Sabeti, P. , & Mitzenmacher, M. (2012). MINE: 
Maximal information-based nonpar ametric explor ation. Re- 
trie v ed fr om http:// www.exploredata.net/ Downloads/ P- Value- Ta 
bles .
Sun , Q., Jiang, B., Zhu, H., & Ibrahim, J. G. (2019). Hard thresholding 
r egr ession. Scandinavian J ournal of Statistics , 46 (1), 314–328. https: 
// doi.org/ 10.1111/ sjos.12353 .
T an , C., Lv , S. , Dong, F. , & Takei, M. (2018). Image reconstruction based 
on convolutional neural network for electrical resistance tomog- 
r a phy. IEEE Sensors J ournal , 19 (1), 196–204. https:// doi.org/ 10.1109/ 
JSEN.2018.2876411 .
Ta ylor , B. (2013). T hor Flight 98. Retrie v ed fr om the Univ ersity of Min- 
nesota Digital Conservancy. https://hdl.handle.net/11299/17437 
5 .
Taylor , B. (2014). Thor Flight 104. Retrie v ed fr om the Univ ersity of 
Minnesota Digital Conservancy. https://hdl.handle.net/11299/1 
74228 .
Theissler , A. (2017). Detecting kno wn and unkno wn faults in au- 
tomotive systems using ensemble-based anomaly detection. 
Knowledge-Based Systems , 123 , 163–173. https:// doi.org/ 10.1016/ j. 
knosys.2017.02.023 .
W ang , B . , Liu, D. , Peng, X. , & Wang, Z. (2019). Data-driv en anomal y de- 
tection of UAV based on multimodal regression model. In Proceed- 
ings of the 2019 IEEE International Instrumentation and Measurement 
Tec hnolog y Conference (I2MTC) (pp. 1–6). IEEE. https:// doi.org/ 10.110 
9/I2MTC.2019.8827154 .
W ang , B . , Liu, D. , Peng, Y. , & Peng, X. (2019). Multivariate regression- 
based fault detection and r ecov ery of UAV flight data. IEEE Trans- 
actions on Instrumentation and Measurement , 69 (6), 3527–3537. https: 
// doi.org/ 10.1109/ TIM.2019.2935576 .
W ang , B . , Peng, X. , Jiang, M. , & Liu, D. (2020). Real-time fault detection 
for UAV based on model acceleration engine. IEEE Transactions on 
Instrumentation and Measurement , 69 (12), 9505–9516. https://doi.or 
g/ 10.1109/ TIM.2020.3001659 .
W ang , B ., W ang, Z. , Liu, L. , Liu, D. , & Peng, X. (2019). Data-driven 
anomaly detection for UAV sensor data based on deep learning 
prediction model. In Proceedings of the 2019 Prognostics and Sys- 
tem Health Management Conference (PHM-P aris) (pp . 286–290). IEEE. 
https:// doi.org/ 10.1109/ PHM-Paris.2019.00055 .
Wang , Y., Chen, W., Luan, T. H., Su, Z., Xu, Q., Li, R., & Chen, N. (2022). 
Task offloading for post-disaster rescue in unmanned aerial ve- 
hicles networks. IEEE/ACM Transactions on Networking , 30 (4), 1525–
1539. https:// doi.org/ 10.1109/ TNET.2022.3140796 .
Wu , H. , Hu, T. , Liu, Y. , Zhou, H. , Wang, J. , & Long, M. (2022). TimesNet: 
Tempor al 2D-v ariation modeling for gener al time series anal y- 
sis. arXiv Preprint arXiv:2210.02186 . https:// doi.org/ 10.48550/arX 
iv.2210.02186 .
Yang , L. , Li, S. , Li, C. , Zhang, A. , & Zhang, X. (2023). A survey of un- 
manned aerial vehicle flight data anomal y detection: Tec hnolo- 
gies , applications , and futur e dir ections. Science China Tec hnological 
Sciences , 66 (4), 901–919. https:// doi.org/ 10.1007/ s11431- 022- 2213- 
8 .
Yang , L., Li, S., Li, C., Zhu, C., Zhang, A., & Liang, G. (2023). Data- 
driv en unsupervised anomal y detection and r ecov ery of un- 
manned aerial vehicle flight data based on spatiotemporal corre- 
lation. Science China Technological Sciences , 66 (5), 1304–1316. https: 
// doi.org/ 10.1007/ s11431- 022- 2312- 8 .
Zhai , Q., & Ye, Z. S. (2020). How reliable should military UAVs be?. 
IISE Transactions , 52 (11), 1234–1245. https:// doi.org/ 10.1080/ 2472 
5854.2019.1699977 .
Zhong , J. , Zhang, Y. , Wang, J. , Luo , C. , & Miao , Q. (2022). Unmanned 
aerial vehicle flight data anomaly detection and recovery predic- 
tion based on spatio-tempor al corr elation. IEEE Transactions on Re- 
liability , 71 (1), 457–468. https:// doi.org/ 10.1109/ TR.2021.3134369 .
Recei v ed: October 17, 2023. Revised: Mar c h 7, 2024. Accepted: Mar c h 7, 2024 
© The Author(s) 2024. Published by Oxford Uni v ersity Pr ess on behalf of the Society for Computational Design and Engineering. This is an Open Access article distributed 
under the terms of the Cr eati v e Commons Attribution-NonCommercial License ( https://creativecommons.org/licenses/by-nc/4.0/ ), which permits non-commercial re-use, 
distribution, and r e pr oduction in any medium, pr ovided the original work is pr operl y cited. For commercial r e-use, please contact journals.permissions@oup.com 
Downloaded from https://academic.oup.com/jcde/article/11/2/176/7627449 by Netaji Subhas University of Technology user on 07 April 2026
