# A Safety Modulator Actor-Critic Method in Model-Free Safe Reinforcement Learning and Application in UAV Hovering,.pdf

## Page 1

Contents lists available at ScienceDirect
Journal of the Franklin Institute
journal homepage: www.elsevier.com/locate/fi
A safety modulator actor-critic method in model-free safe 
reinforcement learning and application in UAV hovering 
Qihan Qi a, Xinsong Yang
a,∗, Daniel W C Ho b, Yaping Sun a
a College of Electronics and Information Engineering, Sichuan University, 610065, Chengdu, China
b Department of Mathematics, City University of Hong Kong, Kowloon, Hong Kong
a r t i c l e  i n f o
Keywords:
Distributional critic
Overestimation mitigation
Safe reinforcement learning
Safety modulator
 
a b s t r a c t
This paper proposes a safety modulator actor-critic (SMAC) method to address safety constraint 
and overestimation mitigation in model-free safe reinforcement learning (RL). A safety modulator 
is developed to satisfy safety constraints by modulating actions, allowing the policy to ignore 
safety constraint and focus on maximizing reward. Additionally, a distributional critic with a 
theoretical update rule for SMAC is proposed to mitigate the overestimation of Q-values with 
safety constraints. Both simulation and real-world scenarios experiments on Unmanned Aerial 
Vehicles (UAVs) hovering and ﬁgure-8 tracking conﬁrm that the SMAC can eﬀectively maintain 
safety constraints and outperform mainstream baseline algorithms.
1.  Introduction
Reinforcement learning (RL) has demonstrated remarkable achievements in controlled environments like games and simulations 
[1–6] since results derived from it are rarely fail.  However, deploying RL in real-world and safety-critical systems, e.g. UAVs, presents 
a formidable challenge, where the core diﬃculty lies in solving two fundamental and often conﬂicting problems simultaneously: 
(1) Guaranteeing safety by strictly adhering to operational constraints; (2) Ensuring learning stability by mitigating the inherent 
overestimation bias in actor-critic methods. In the literature, these two fundamental challenges have often been addressed separately.
Ensuring safety is commonly addressed by using two main paradigms in safe RL [7]: safety ﬁlter method [8,9] and safety learning 
method [10–14]. The safety ﬁlter method solves the safety problem by using a safety ﬁlter on the actions of the RL agent [8,9]. 
Although the safety ﬁlter can transform unsafe actions into safe actions, it neither guarantees safety nor oﬀers adaptability [8] or 
even requires extremely precise information of a dynamic model for constructing safety ﬁlter [9]. Therefore, achieving satisfactory 
safety performance by using safety ﬁlters in practical systems remains challenging, and it is more diﬃcult when diﬀerent tasks 
require diverse modeling approaches, particularly for tasks that lack existing models. In contrast, the safety methods in learning 
optimizes the policy with safety constraints throughout the learning process directly. An advantage of safety learning methods is 
their model-free nature, which allows them to be applied to complex systems without requiring an accurate system model. This is 
particularly beneﬁcial in real-world scenarios where accurate models are often diﬃcult or impossible to obtain. A notable safety 
in learning method is the Lagrangian method [10,11], which transforms an optimization problem with safety constraints into an 
unconstrained primal-dual optimization problem. This is achieved by dynamically adjusting the weight of the safety cost rewards 
based on the degree of satisfaction with safety constraints.  However, the Lagrangian method introduces a critical diﬃculty: The 
policy is burdened with a trade-oﬀ between maximizing rewards and minimizing safety costs. This coupling can compromise both 
∗Corresponding author.
 
E-mail addresses: qiqihan@stu.scu.edu.cn (Q. Qi), xinsongyang@163.com (X. Yang), madaniel@cityu.edu.hk (D.WC Ho), 
sunyaping@scu.edu.cn (Y. Sun).
https://doi.org/10.1016/j.jfranklin.2025.108158
Received 24 June 2025; Received in revised form 26 September 2025; Accepted 16 October 2025
Journal of the Franklin Institute 362 (2025) 108158 
Available online 19 October 2025 
0016-0032/© 2025 The Franklin Institute. Published by Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, 
and similar technologies.

## Page 2

Q. Qi et al.
objectives, leading to suboptimal performance or even learning failures, especially in complex tasks. Hence, it is urgent to develop 
new techniques to alleviate the burden of policy while meeting safety constraints.
On the other hand, overestimation is a well-known challenge in many RL algorithms where the agent learns inﬂated Q-values, 
which leads to suboptimal and unstable policies [15–17]. In practice, overestimation is inevitable, just as what has been demonstrated 
in [15] that system noise, approximation error, or any other sources can induce an overestimation bias. To mitigate overestimation, 
approaches like double Q-learning and double Q-network were developed by [15,18] to leverage a target Q-network to provide 
unbiased estimates. However, these methods are inherently limited to discrete action spaces. Although the authors in [19] extend 
double Q-learning and Q-network to continuous action spaces by using actor-critic method, the overestimation problem persists 
due to the high similarity between the online Q-value and the target Q-value. While distributional critic approaches have been 
employed [11,20], these methods lack theoretical analysis to derive a gradient update rule that addresses overestimation. Although 
[17] eﬀectively mitigates overestimation with a theoretically guaranteed gradient update rule, their approach fails to address safety 
constraints, let alone alleviate the burden of policy in meeting safety constraints. These gaps motivate us to propose a novel method 
to investigate the mitigation of overestimation and the alleviation of policy burden in safe RL.
To address the challenges of safety constraint satisfaction and overestimation mitigation with a uniﬁed approach, this paper 
proposes a novel SMAC method to address the issues of both safety constraints and mitigate overestimation. A safety modulator is 
introduced to modulate the action of policy, which alleviates the burden of policy and allows the policy to concentrate on maximizing 
the reward while disregarding the trade-oﬀ for cost rewards. The main contributions are as follows.
(1) A model-free safety modulator is presented to modulate the action of policy, which enables the policy to neglect cost rewards and 
focus on maximizing rewards. Without the safety modulator, the policies in [10,11] may suﬀer failures in the learning process 
because they always need to trade oﬀ the maximization of rewards against cost rewards.
(2) To mitigate overestimation, a distributional critic for SMAC is proposed to incorporate distributional information with theo-
retically updated rules to mitigate overestimation under safety constraints. Diﬀerent from existing papers, the overestimation 
mitigation approach is given by detailed theoretical analysis.
(3) Both PyBullet simulations and real-world experiments for UAV hovering and ﬁgure-8 tracking demonstrate that the proposed 
SMAC algorithm can eﬀectively mitigate overestimation while maintaining safety constraints. Comparative experiments show 
the merit that our algorithm outperforms the mainstream baseline algorithms in [21,22].
The rest is organized as follows. The related work is introduced in Section 2. Section 3 presents the safety modulator for safe 
RL. Section 4 analyzes the overestimation problem and mitigates overestimation with the distributional critic. In Section 5 proposes 
the SMAC algorithm in detail. Section 6 presents the UAV hovering and ﬁgure-8 tracking tasks to show the SMAC’s eﬃcacy. Finally, 
Section 7 draws the conclusion.
2.  Related work
2.1.  Constrained Markov decision process
Safe RL problem is often modeled as a Constrained Markov Decision Process (CMDP), which extends the standard Markov Decision 
Process (MDP) framework. While a standard MDP’s objective is solely to learn a policy that maximizes a cumulative reward, a CMDP 
introduces an additional cost function and a corresponding constraint.
Formally, a CMDP [23,24] is deﬁned as a tuple (𝑋, 𝑈, 𝑟, 𝑟𝑐, 𝑝), where 𝑋 and 𝑈 are the continuous state space and continuous 
action space, respectively, 𝑟∶𝑋× 𝑈→[𝑟min, 𝑟max] is the reward function, 𝑟𝑐∶𝑋× 𝑈→[𝑐min, 𝑐max] is the cost reward function, 𝑝∶
𝑋× 𝑈× 𝑋→[0, 1] is the state transition function. It is assumed that the state 𝑥𝑡∈𝑋 at time 𝑡 can be observed from the environment, 
the agent takes an action 𝑢𝑡∈𝑈 to interact with the environment and transmit state 𝑥𝑡 to 𝑥𝑡+1. The initial state 𝑥0 ∼, is the initial 
state distribution, 𝜋(⋅|𝑥𝑡) is the action policy distribution under state 𝑥𝑡 and action 𝑢𝑡∼𝜋(⋅|𝑥𝑡). The entire trajectory distribution under 
policy 𝜋 is represented as 𝑇𝜋= (𝑥0, 𝑢0, 𝑥1, 𝑢1, ⋯). The goal of safe RL is to optimize the following problem:
max
𝜋
𝔼
[ ∞
∑
𝑡=0
𝛾𝑡𝑟(𝑥𝑡, 𝑢𝑡)
]
,
(1)
s.t. 𝔼
[ ∞
∑
𝑡=0
𝛾𝑡𝑟𝑐(𝑥𝑡, 𝑢𝑡)
]
≤𝐶,
where 𝑟(𝑥𝑡, 𝑢𝑡) is the reward function and 𝑟𝑐(𝑥𝑡, 𝑢𝑡) is the cost reward function, 𝐶≥0 is the given safety constraint, 𝛾 is the discount 
factor of reward and cost reward. 
2.2.  Soft actor-Critic with lagrangian
Soft Actor-Critic (SAC) [21] is a state-of-the-art, oﬀ-policy reinforcement learning algorithm for continuous control. It optimizes 
a policy to maximize a trade-oﬀ between expected reward and entropy, which encourages exploration and leads to stable training, 
making it a widely-used baseline.
Journal of the Franklin Institute 362 (2025) 108158 
2

## Page 3

Q. Qi et al.
To handle safety constraints, SAC is often extended into SAC-Lagrangian (SAC-Lag) [22] by incorporating the Lagrangian method 
[10,11]. This method transforms the constrained optimization problem of Eq. (1) into an unconstrained dual objective: 
min
𝜆≥0 max
𝜋
𝔼
[ ∞
∑
𝑡=0
𝛾𝑡𝑟(𝑥𝑡, 𝑢𝑡) −𝜆
( ∞
∑
𝑡=0
𝛾𝑡𝑟𝑐(𝑥𝑡, 𝑢𝑡) −𝐶
)]
,
(2)
where 𝜆≥0 denotes the safety weight and is dynamically adjusted according to the satisfaction of constraints.
The goal of SAC-Lag is to learn a policy that can simultaneously maximize rewards and minimize costs. However, it faces a primary 
weakness: the policy is forced to solve a diﬃcult trade-oﬀ between these often conﬂicting goals within a single, monolithic objective, 
which can ultimately overburden the agent. This burden can lead to learning instability or failure, which motivates us to decouple 
these competing goals by using a safety modulator. 
3.  Safety modulator
As what has been discussed in the previous section, traditional Lagrangian-based RL methods such as SAC-Lag solve the safe RL 
problem Eq. (1) by optimizing a single, combined objective Eq. (2), which usually lead to overburden of the policy and instability. To 
solve this problem, this work proposes a novel approach that decouples the optimization of reward-seeking and safety-enforcement.
We begin by re-expressing the standard Lagrangian objective in terms of state-action value functions. Deﬁne the expected cumu-
lative reward 𝑄(𝑥𝑡, 𝑢𝑡) and cost 𝑄𝑐(𝑥𝑡, 𝑢𝑡) as follows: 
𝑄(𝑥0, 𝑢0) = 𝔼
∞
∑
𝑡=0
𝛾𝑡𝑟(𝑥𝑡, 𝑢𝑡), 𝑄𝑐(𝑥0, 𝑢0) = 𝔼
∞
∑
𝑡=0
𝛾𝑡𝑟𝑐(𝑥𝑡, 𝑢𝑡).
Then, for a given state-action pair (𝑥0, 𝑢0), the unconstrained optimization problem (2) can be simpliﬁed as: 
min
𝜆≥0 max
𝜋
𝔼[𝑄(𝑥0, 𝑢0) −𝜆(𝑄𝑐(𝑥0, 𝑢0) −𝐶)].
(3)
In order to solve (3), two steps are needed: The ﬁrst step is to optimize policy 𝜋 for given 𝜆 and second step is to optimize 𝜆 for 
given 𝜋:
Step 1: max
𝜋
𝔼[𝑄(𝑥0, 𝑢0) −𝜆(𝑄𝑐(𝑥0, 𝑢0) −𝐶)],
(4)
Step 2: min
𝜆≥0 𝔼[−𝜆(𝑄𝑐(𝑥0, 𝑢0) −𝐶)].
(5)
Remark 1. According to the contraction mapping theorem in [25], a unique ﬁxed point exists in a complete metric space. By 
continuously applying the contraction mapping, starting from any initial state 𝑥0 and 𝑢0 ∼𝜋(⋅|𝑥0), this unique ﬁxed point can be 
reached. Consequently, policy iteration will converge to the optimal value function regardless of the initial estimates. For oﬀ-policy 
training, the optimization (4) can be represented as max
𝜋
𝔼[𝑄(𝑥𝑡, 𝑢𝑡) −𝜆(𝑄𝑐(𝑥𝑡, 𝑢𝑡) −𝐶)]. 
In order to address (4) for the action 𝑢𝑡∼𝜋(⋅|𝑥𝑡), one can maximize 𝑄(𝑥𝑡, 𝑢𝑡) and minimize 𝑄𝑐(𝑥𝑡, 𝑢𝑡). In the training step, the 
policy constantly trades oﬀ the 𝑄(𝑥𝑡, 𝑢𝑡) against the 𝑄𝑐(𝑥𝑡, 𝑢𝑡). Consequently, it may face a signiﬁcant challenge or failure in its task 
learning. To prevent this from happening, the safety modulator Δ𝑢𝑡 and modulation function 𝑚(⋅) ∶𝐴→𝐴 are presented such that 
𝑢𝑡= 𝑚(̄𝑢𝑡, Δ𝑢𝑡), where ̄𝑢𝑡∼𝜋𝜃𝑢(⋅|𝑥𝑡) is the risky policy that disregards the potential for unsafe situations, Δ𝑢𝑡∼𝜋𝜃Δ(⋅|𝑥𝑡, ̄𝑢𝑡) is the safety 
modulator for ̄𝑢𝑡, 𝜋𝜃̄𝑢(⋅|𝑥𝑡) and 𝜋𝜃Δ(⋅|𝑥𝑡, ̄𝑢𝑡) denote the policy approximated with parameters 𝜃̄𝑢 and 𝜃Δ, respectively. In the following 
statement, the overall composed policy will be denoted as 𝜋𝜃𝑢∙𝜃Δ.
For the model training, the risky policy 𝜋𝜃̄𝑢, safety modulator 𝜋𝜃Δ and critics 𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡), 𝑄𝑐,𝑤𝑐(𝑥𝑡, 𝑢𝑡) are learned from experience 
tuple (𝑥𝑡, 𝑢𝑡, 𝑟(𝑥𝑡, 𝑢𝑡), 𝑟𝑐(𝑥𝑡, 𝑢𝑡), 𝑥𝑡+1) ∼𝐷, where 𝐷 represents the replay buﬀer, 𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) and 𝑄𝑐,𝑤𝑐(𝑥𝑡, 𝑢𝑡) are the approximations of 
𝑄(𝑥𝑡, 𝑢𝑡) and 𝑄𝑐(𝑥𝑡, 𝑢𝑡) using the parameters 𝑤𝑞 and 𝑤𝑐, respectively. Introducing safety modulator, (4) can be divided into two parts:
max
𝜃̄𝑢
𝔼𝑄𝑤𝑞(𝑥𝑡, ̄𝑢𝑡),
(6)
max
𝜃Δ
𝔼[−𝑑(𝑢𝑡, ̄𝑢𝑡) −𝜆𝑄𝑐,𝑤𝑐(𝑥𝑡, 𝑢𝑡)],
(7)
where 𝑑(𝑢𝑡, ̄𝑢𝑡) = 1
2‖𝑢𝑡−̄𝑢𝑡‖2 is the distance function between ̄𝑢𝑡 and 𝑢𝑡. Compared to the formulation in (4), the decomposition in (7) 
relieves the policy 𝜋𝜃̄𝑢 from the need to balance the trade-oﬀ between reward maximization and safety assurance. As a result, 𝜋𝜃̄𝑢 can 
focus solely on maximizing rewards. The safety modulator, 𝜋𝜃Δ, is then responsible for safety by adjusting the action to minimize 
the safety cost 𝑄𝑐,𝑤𝑐, while simultaneously minimizing the deviation from the original action ̄𝑢𝑡. This decoupled design simpliﬁes the 
policy training process compared to the monolithic optimization in (4). The detailed framework of policy ̄𝑢𝑡 and modulator Δ𝑢𝑡 is 
depicted in Fig. 1.
Remark 2. The modulation function 𝑚(̄𝑢𝑡, Δ𝑢𝑡) is deﬁned as 𝑢𝑡= 𝑚(̄𝑢𝑡, Δ𝑢𝑡) = clip(̄𝑢𝑡+ Δ𝑢𝑡, −𝑢max, 𝑢max), where 𝑢max is the upper bound 
of action space, clip(⋅) is the function to constrain the values of ̄𝑢𝑡+ Δ𝑢𝑡 within a speciﬁed range [−𝑢max, 𝑢max]. The modulation 
function can provide both ﬂexibility and control in modifying actions, and hence, it is suitable for varying conditions by using an 
easy-to-implement additive safety modulator while ensuring that modiﬁcations remain within safe and acceptable boundaries. 
Journal of the Franklin Institute 362 (2025) 108158 
3

## Page 4

Q. Qi et al.
Fig. 1. The decoupled training framework for policy ̄𝑢𝑡 and modulator Δ𝑢𝑡. The policy 𝜋𝜃̄𝑢 is exclusively trained to maximize the total reward 𝑄𝑤𝑞, 
as indicated by the orange gradient path. Independently, the safety modulator 𝜋𝜃Δ is trained to minimize safety costs and action deviation, guided 
by the gradients shown in purple. (For interpretation of the references to colour in this ﬁgure legend, the reader is referred to the web version of 
this article.)
Remark 3. To introduce the safety modulator that allows the policy to concentrate on maximizing the reward, it is necessary to 
transform (4) into (7). However, the policies in [10,11] fail to derive (7) as they cannot establish the connection between ̄𝑢 and Δ𝑢. 
This paper addresses this issue by constructing the distance 𝑑(𝑢𝑡, ̄𝑢𝑡) = 1
2|𝑢𝑡−̄𝑢𝑡|2, which enables the safety modulator to minimize 
this distance, thereby adjusting ̄𝑢 as minimally as possible while still ensuring it meets certain constraints to guarantee the action’s 
safety. 
The safety weight 𝜆 in (5) can be optimized by minimizing the following loss 𝐽(𝜆) with the entire 𝐌 steps episode state-action 
pairs {(𝑠𝑖, 𝑎𝑖)}𝐌−1
𝑖=0
∼𝑇𝜋𝜃𝑢∙𝜃Δ , 
𝐽𝜆(𝜆) = 𝜆(𝐶−
𝐌−1
∑
𝑡=0
𝛾𝑡𝑟𝑐(𝑥𝑡, 𝑢𝑡)).
(8)
After each rollout, we collect a batch of cost rewards to guarantee that the safety constraint is strictly satisﬁed. The 𝜆 is only 
updated after collecting the entire episode state-action pairs.
4.  Overestimation mitigation
In this section, the issue of overestimation inherent in Q-learning is discussed, and speciﬁc overestimation value is provided through 
formula derivation. After that, the distributional critic and corresponding update rule are introduced to mitigate overestimation.
The Q-value approximated by the parameter 𝑤𝑞 is expressed as 𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) = 𝑄(𝑥𝑡, 𝑢𝑡) + 𝜈𝑡 with 𝜈𝑡 being a random zero mean noise, 
𝑄(𝑥𝑡, 𝑢𝑡) is the ideal Q-value without bias. Then, the updated parameter 𝑤′
𝑞 can be obtained by the following formula 
𝑤′
𝑞= 𝑤𝑞+ 𝜂(𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡),
where 𝜂 is the learning rate which controls update step size, 𝑦= 𝔼[𝑟(𝑥𝑡, 𝑢𝑡) + 𝛾max
𝑢𝑡+1 𝑄𝑤𝑞(𝑥𝑡+1, 𝑢𝑡+1)] is the Bellman equation.
For the purpose of analysis, we introduce a hypothetical updated parameter 𝑤′
𝑞, which represents the parameter vector that would 
be obtained if the update are performed using the ideal, unbiased target value 𝑦: 
𝑤′
𝑞= 𝑤𝑞+ 𝜂(𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡),
where 𝑦= 𝔼[𝑟(𝑥𝑡, 𝑢𝑡) + 𝛾max
𝑢𝑡+1 𝑄(𝑥𝑡+1, 𝑢𝑡+1)] is the ideal value of 𝑦.
Denote 𝑄𝑤′𝑞(𝑥𝑡, 𝑢𝑡) and 𝑄𝑤′
𝑞(𝑥𝑡, 𝑢𝑡) as the Q-value approximated by the parameter 𝑤′
𝑞 and 𝑤′
𝑞, respectively. Our primary objective 
is to formally analyze the estimation error introduced during this single learning step. This error can be quantiﬁed by the diﬀerence 
between the Q-value obtained from the actual update 𝑄𝑤′𝑞(𝑥𝑡, 𝑢𝑡) and the Q-value that would have been obtained from the ideal update 
𝑄𝑤′
𝑞(𝑥𝑡, 𝑢𝑡). However, the relationship between a parameter update from 𝑤𝑞 to 𝑤′
𝑞 and the resulting change in the Q-function’s output 
is implicit and non-linear, which is direct comparison diﬃcult.
To bridge this gap, we ﬁrst employ the ﬁrst-order Taylor’s expansion to approximate the Q-value after a parameter update. The 
linear approximation of the Q-value at the update parameters 𝑤′
𝑞 and 𝑤′
𝑞 is obtained by expanding the Q-value around the current 
parameter 𝑤𝑞, as follows:
𝑄𝑤′𝑞(𝑥𝑡, 𝑢𝑡) ≈𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) + ∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)⊤(𝑤′
𝑞−𝑤𝑞),
𝑄𝑤′
𝑞(𝑥𝑡, 𝑢𝑡) ≈𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) + ∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)⊤(𝑤′
𝑞−𝑤𝑞).
Journal of the Franklin Institute 362 (2025) 108158 
4

## Page 5

Q. Qi et al.
From the gradient update rule, the term (𝑤′
𝑞−𝑤𝑞) and (𝑤′
𝑞−𝑤𝑞) are equal to 𝜂(𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) and 𝜂(𝑦−
𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡), respectively. By substituting this into the above equations, we obtain:
𝑄𝑤′𝑞(𝑥𝑡, 𝑢𝑡) ≈𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) + 𝜂(𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))
‖∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)‖2,
(9)
𝑄𝑤′
𝑞(𝑥𝑡, 𝑢𝑡) ≈𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) + 𝜂(𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))
‖∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)‖2.
(10)
Then, the estimation error of 𝑄𝑤𝑞 during an update step is
𝜀(𝑥𝑡, 𝑢𝑡) = 𝔼[𝑄𝑤′𝑞(𝑥𝑡, 𝑢𝑡) −𝑄𝑤′
𝑞(𝑥𝑡, 𝑢𝑡)]
≈𝔼[𝜂(𝑦−𝑦)‖∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)‖2]
= 𝜂𝛾𝔼[max
𝑢𝑡+1 𝑄𝑤𝑞(𝑥𝑡+1, 𝑢𝑡+1) −max
𝑢𝑡+1 𝑄(𝑥𝑡+1, 𝑢𝑡+1)]‖∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)‖2.
Considering 𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) = 𝑄(𝑥𝑡, 𝑢𝑡) + 𝜈𝑡 and letting 𝜖= 𝔼[max
𝑢𝑡+1 [𝑄(𝑥𝑡+1, 𝑢𝑡+1) + 𝜈𝑡+1] −max
𝑢𝑡+1 𝑄(𝑥𝑡+1, 𝑢𝑡+1)], one has 
𝜀(𝑥𝑡, 𝑢𝑡) ≈𝜂𝛾𝜖‖∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)‖2.
It is noteworthy that 𝜖≥0 [18], which implies 𝜀(𝑥𝑡, 𝑢𝑡) ≥0, i.e., the max operator inherently introduces an upward bias to esti-
mation errors. Even if a single update introduces only a slight upward bias, the cumulative eﬀect of these bias through temporal 
diﬀerence (TD) learning can lead to substantial overestimation, which makes the policy suboptimal.
To mitigate overestimation, a distributional critic denoted by (𝑥𝑡, 𝑢𝑡) is considered, which follows a normal distribution 𝑍(⋅|𝑥𝑡, 𝑢𝑡). 
The mean and standard deviation of this distribution are approximated by the neural network outputs 𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) and 𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡), 
respectively.
Deﬁne 𝑍(⋅|𝑥𝑡, 𝑢𝑡) = 𝑁(𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡), 𝜎2
𝑤𝜎(𝑥𝑡, 𝑢𝑡)). Consider the distributional Bellman equation ̃𝑦= 𝑟+ 𝛾(𝑥𝑡+1, 𝑢𝑡+1), where 𝑢𝑡+1 =
arg max
𝑢𝑡+1 𝑄𝑤𝑞(𝑥𝑡+1, 𝑢𝑡+1). Assuming ̃𝑦∼𝑍(⋅|𝑥𝑡, 𝑢𝑡) with 𝑍(⋅|𝑥𝑡, 𝑢𝑡) being the ideal normal distribution, one has 
𝔼[̃𝑦] = 𝔼[𝑟(𝑥𝑡, 𝑢𝑡) + 𝛾max
𝑢𝑡+1 𝑄𝑤𝑞(𝑥𝑡+1, 𝑢𝑡+1)] = 𝑦.
For convenience of later study, let 𝑍(⋅|𝑥𝑡, 𝑢𝑡) = 𝑁(𝑦, 𝜎2), where 𝜎 represents the ideal standard deviation. To measure the distance 
between 𝑍(⋅|𝑥𝑡, 𝑢𝑡) and 𝑍(⋅|𝑥𝑡, 𝑢𝑡), the Kullback-Leibler (KL) divergence [17,26,27] is utilized. Since both the distributions are normal, 
the KL divergence can be analytically expressed as follows 
𝐷𝐾𝐿(𝑍(⋅|𝑥𝑡, 𝑢𝑡), 𝑍(⋅|𝑥𝑡, 𝑢𝑡)) = log
𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡)
𝜎
+
𝜎2(𝑥𝑡, 𝑢𝑡) + (𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))2
2𝜎2
𝑤𝜎(𝑥𝑡, 𝑢𝑡)
−1
2 .
(11)
As a result,  let 𝛿𝑤𝑞= ̃𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡), the parameters 𝑤𝑞 and 𝑤𝜎 are updated as follows
𝑤′
𝑞= 𝑤𝑞+ 𝜂∇𝑤𝑞𝐷𝐾𝐿(𝑍(⋅|𝑥𝑡, 𝑢𝑡), 𝑍(⋅|𝑥𝑡, 𝑢𝑡))
= 𝑤𝑞+ 𝜂
̃𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)
𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡)2
∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)
= 𝑤𝑞+ 𝜂
𝛿𝑤𝑞
𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡)2 ∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡),
(12)
𝑤′
𝜎= 𝑤𝜎+ 𝜂∇𝑤𝜎𝐷𝐾𝐿(𝑍(⋅|𝑥𝑡, 𝑢𝑡), 𝑍(⋅|𝑥𝑡, 𝑢𝑡))
= 𝑤𝜎+ 𝜂
𝜎2 −𝜎2
𝑤𝜎(𝑥𝑡, 𝑢𝑡) + (𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))2
𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡)3
∇𝑤𝜎𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡).
(13)
Additionally, there exists an ideal target ̃𝑦, denoted as ̃𝑦, such that 𝔼[̃𝑦] = 𝔼[𝑟(𝑥𝑡, 𝑢𝑡) + 𝛾max
𝑢𝑡+1 𝑄(𝑥𝑡+1, 𝑢𝑡+1)] = 𝑦. Following a similar 
derivation to the KL divergence (11), the update for 𝑤′
𝑞 is given by 
𝑤′
𝑞= 𝑤𝑞+ 𝜂
𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)
𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡)2
∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡).
(14)
In a manner similar to the derivation of 𝜀(𝑥𝑡, 𝑢𝑡), the overestimation bias of 𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) in the distributional critic (𝑥𝑡, 𝑢𝑡) can be 
expressed as 
̃𝜀(𝑥𝑡, 𝑢𝑡) =
𝜀(𝑥𝑡, 𝑢𝑡)
𝜎2
𝑤𝜎(𝑥𝑡, 𝑢𝑡).
(15)
Journal of the Franklin Institute 362 (2025) 108158 
5

## Page 6

Q. Qi et al.
Remark 4. According to (15), the overestimation bias ̃𝜀(𝑥𝑡, 𝑢𝑡) is inversely proportional to 𝜎2
𝑤𝜎(𝑥𝑡, 𝑢𝑡). It is obvious that once 
𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡) ≥1, the condition ̃𝜀(𝑥𝑡, 𝑢𝑡) ≤𝜀(𝑥𝑡, 𝑢𝑡) can be guaranteed, and hence the overestimation can be mitigated. Therefore, we 
choose 𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡) = max(𝜎𝑤𝜎(𝑥𝑡, 𝑢𝑡), 𝜎min), where 𝜎min ≥1 is a given parameter. 
Remark 5. It should be noted that the safety constraint 𝐶 is a given deterministic constant. Intuitively, using a distributional cost 
critic to evaluate the deterministic 𝑄𝑐(𝑥𝑡, 𝑢𝑡) is unsuitable. Therefore, we only use a distributional critic for 𝑄(𝑥𝑡, 𝑢𝑡). 
5.  Safety modulator actor-critic
This section proposes an SMAC algorithm, incorporating the corresponding update rules for the risky policy 𝜋𝜃̄𝑢(⋅|𝑥𝑡), the safety 
modulator 𝜋𝜃Δ(⋅|𝑥𝑡, ̄𝑢𝑡), the distributional critic 𝑍𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡), and the cost critic 𝑄𝑐,𝑤𝑐(⋅|𝑥𝑡, 𝑢𝑡), with approximate parameters 𝜃̄𝑢, 𝜃Δ, 𝑤𝑞, 
and 𝑤𝑐. It is noteworthy that the update rule of the distributional critic in Distributional Policy Evaluation can theoretically guarantee 
overestimation mitigation. Additionally, a series of training techniques are employed in Distributional Policy Evaluation to improve 
training stability. The updated rule of the safety modulator is detached from the gradient 𝜃̄𝑢 to alleviate the burden of risky policy to 
focus on maximizing rewards.
5.1.  Safety policy evaluation
5.1.1.  Distributional policy evaluation
Considering 𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡) ∼𝜋̃𝜃̄𝑢∙̃𝜃Δ 𝑍̃𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡), (𝑥𝑡, 𝑢𝑡) ∼𝐷, the loss function of KL divergence is given as
𝐽𝑧(𝑤𝑞) = 𝔼[𝐷𝐾𝐿(𝜋̃𝜃̄𝑢∙̃𝜃Δ 𝑍̃𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡), 𝑍𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡))]
= 𝔼
[
∫[log(𝑃(𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡)|𝜋̃𝜃̄𝑢∙̃𝜃Δ 𝑍̃𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡)))
−log(𝑃(𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡)|𝑍𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡)))]
𝑃(𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡)|𝜋̃𝜃̄𝑢∙̃𝜃Δ 𝑍̃𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡))
]
𝑑𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡)
= 𝔼[−log(𝑃(𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡)|𝑍𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡)))] + ℑ,
(16)
where ℑ is independent of the optimized parameter 𝑤𝑞, ̃𝑤𝑞 is the parameter of target distribution 𝑍̃𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡), 𝜋̃𝜃̄𝑢∙̃𝜃Δ  is the Bellman 
operator with policy 𝜋̃𝜃̄𝑢∙̃𝜃Δ, and 𝜋̃𝜃̄𝑢∙̃𝜃Δ is the safe target policy with target parameters ̃𝜃̄𝑢 and ̃𝜃Δ.
In view of 𝑍𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡) = 𝑁(𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡), 𝜎2
𝑤𝑞(𝑥𝑡, 𝑢𝑡)) and 𝛿𝑤𝑞= ̃𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡), the gradient of 𝐽𝑧(𝑤𝑞) is obtained as
∇𝑤𝑞𝐽𝑧(𝑤𝑞) = 𝔼[−∇𝑤𝑞log(𝑃(𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡)|𝑍𝑤𝑞(⋅|𝑥𝑡, 𝑢𝑡)))]
= 𝔼
[
−∇𝑤𝑞log
(exp(−
(𝜋̃𝜃̄𝑢∙̃𝜃Δ
(𝑥𝑡,𝑢𝑡)−𝑄𝑤𝑞(𝑥𝑡,𝑢𝑡))2
2𝜎2𝑤𝑞(𝑥𝑡,𝑢𝑡)
)
√
2𝜋𝜎𝑤𝑞(𝑥𝑡, 𝑢𝑡)
)]
= 𝔼
[
−∇𝑤𝑞
((𝜋̃𝜃̄𝑢∙̃𝜃Δ (𝑥𝑡, 𝑢𝑡) −𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))2
2𝜎2
𝑤𝑞(𝑥𝑡, 𝑢𝑡)
+ log 𝜎𝑤𝑞(𝑥𝑡, 𝑢𝑡) + log
√
2𝜋
)]
= 𝔼
[
−
̃𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)
2𝜎2
𝑤𝑞(𝑥𝑡, 𝑢𝑡)
∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) −
−𝜎2
𝑤𝑞(𝑥𝑡, 𝑢𝑡) + (̃𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))2
𝜎3
𝑤𝑞(𝑥𝑡, 𝑢𝑡)
∇𝑤𝑞𝜎𝑤𝑞(𝑥𝑡, 𝑢𝑡)
]
= 𝔼
[
−
𝛿𝑤𝑞
2𝜎2
𝑤𝑞(𝑥𝑡, 𝑢𝑡) ∇𝑤𝑞𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡) −
−𝜎2
𝑤𝑞(𝑥𝑡, 𝑢𝑡) + (𝛿𝑤𝑞)2
𝜎3
𝑤𝑞(𝑥𝑡, 𝑢𝑡)
∇𝑤𝑞𝜎𝑤𝑞(𝑥𝑡, 𝑢𝑡)
]
.
(17)
Inspired by [17,19], the independent double Q-networks for critic are used, which are 𝑄𝑤1𝑞 and 𝑄𝑤2𝑞. The critic tends to choose 
the smaller mean value between 𝑄𝑤1𝑞 and 𝑄𝑤2𝑞. Meanwhile, the clip function is used in (̃𝑦−𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡))2 to avoid gradient explosion. 
Moreover, the mean value of ̃𝑦 keeps training stable since (𝑥𝑡+1, 𝑢𝑡+1) is sampled from distribution 𝑍(⋅|𝑥𝑡+1, 𝑢𝑡+1). With the help of 
these steps, the corresponding update rule of stable gradient ∇𝑤𝑖𝑞𝐽𝑧(𝑤𝑖
𝑞), 𝑖= 1, 2 can be represented as follows 
∇𝑤𝑖𝑞𝐽𝑧(𝑤𝑖
𝑞) ≈𝔼
[
−
𝛿𝑤𝑖𝑞
2𝜎2
𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡)
∇𝑤𝑖𝑞𝑄𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡) −
−𝜎2
𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡) + (Δ𝑤𝑖𝑞)2
𝜎3
𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡)
∇𝑤𝑖𝑞𝜎𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡)
]
,
(18)
where 𝛿𝑤𝑖𝑞= ̂𝑦min
𝑤𝑞−𝑄𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡), ̂𝑦min
𝑤𝑞 is the minimum double-Q target to mitigate the Q-value overestimation, ̂𝑦min
𝑤𝑞= 𝑟(𝑥𝑡, 𝑢𝑡) +
𝛾min
𝑖=1,2 𝑄𝑤𝑖𝑞(𝑥𝑡+1, 𝑢𝑡+1), 
Δ𝑤𝑖𝑞= clip(̃𝑦min
𝑤𝑞−𝑄𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡), −𝜁̂𝜎𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡), 𝜁̂𝜎𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡)), 
̃𝑦min
𝑤𝑞= 𝑟(𝑥𝑡, 𝑢𝑡) + 𝛾min
𝑖=1,2 𝑤𝑖𝑞(𝑥𝑡+1, 𝑢𝑡+1), 
̂𝜎𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡) =
𝔼[𝜎𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡)], 𝜁 is an adjustable constant to make sure that |̃𝑦𝑤𝑖𝑞−𝑄𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡)| ≤𝜁̂𝜎𝑤𝑖𝑞(𝑥𝑡, 𝑢𝑡). Speciﬁcally, 𝜁= 3 denotes that 3-sigma 
rule in normal distribution.
Journal of the Franklin Institute 362 (2025) 108158 
6

## Page 7

Q. Qi et al.
Remark 6. Although the works in [11,26,27] employ distributional critics, they lack the update rule derived in this paper, rendering 
them unable to theoretically guarantee the mitigation of overestimation. Moreover, the distributional critic utilized in this paper is 
general, enabling the approximation of the critic with a normal distribution, even if the critic does not follow a normal distribution. 
5.1.2.  Cost evaluation
Given double cost return 𝑄𝑐,𝑤𝑖𝑐(𝑥𝑡, 𝑢𝑡), 𝑖= 1, 2, deﬁne loss function 𝐽𝑐(𝑤𝑖
𝑐) as 
𝐽𝑐(𝑤𝑖
𝑐) = 𝔼[1
2 (𝑟𝑐(𝑥𝑡, 𝑢𝑡) + 𝛾
max
𝑢𝑡+1∼𝜋̃𝜃̄𝑢∙̃𝜃Δ
𝑄𝑐, ̃𝑤𝑐(𝑥𝑡+1, 𝑢𝑡+1) −𝑄𝑐,𝑤𝑖𝑐(𝑥𝑡, 𝑢𝑡))2],
where ̃𝑤𝑐 represents the target parameter. The corresponding gradient is given by 
∇𝑤𝑖𝑐𝐽𝑐(𝑤𝑖
𝑐) = 𝔼[(𝑄𝑐,𝑤𝑖𝑐(𝑥𝑡, 𝑢𝑡) −𝑟𝑐(𝑥𝑡, 𝑢𝑡) −𝛾𝑄𝑐, ̃𝑤𝑐(𝑥𝑡, 𝑢𝑡))∇𝑤𝑐𝑄𝑐,𝑤𝑐(𝑥𝑡, 𝑢𝑡)].
Algorithm 1 SMAC Algorithm.
 Input: Initialized network parameters 𝜃̄𝑢, ̃𝜃̄𝑢, 𝜃Δ, ̃𝜃Δ, 𝑤𝑖
𝑞, ̃𝑤𝑞, 𝑤𝑖
𝑐, ̃𝑤𝑐, 𝑖= 1, 2, target update rate 𝜏, learning rate 𝜂̄𝑢, 𝜂Δ𝑢, 𝜂𝑞, 𝜂𝑐, 𝜂𝜆, 
total training steps 𝐌, safety weight update frequency 𝑘.
 Output: Safe policy 𝜋𝜃̄𝑢∙𝜃Δ𝑢. 
1: Set current training step 𝐦= 0
2: while 𝐦< 𝐌 do
3:
Observe state 𝑥𝑡
4:
Select action ̄𝑢𝑡∼𝜋𝜃̄𝑢(⋅|𝑥𝑡) and safe modulation action Δ𝑢𝑡∼𝜋𝜃Δ𝑢(⋅|𝑥𝑡, ̄𝑢𝑡)
5:
Calculate 𝑢𝑡= 𝑚(̄𝑢𝑡, Δ𝑢𝑡)
6:
Observe reward 𝑟(𝑥𝑡, 𝑢𝑡), cost reward 𝑟𝑐(𝑥𝑡, 𝑢𝑡) and next state 𝑥𝑡+1
7:
Store tuple (𝑥𝑡, 𝑢𝑡, 𝑟(𝑥𝑡, 𝑢𝑡), 𝑟𝑐(𝑥𝑡, 𝑢𝑡), 𝑥𝑡+1) in Replay Buﬀer 𝐷
8:
if rollout and (𝐦mod 𝑘) == 0 then
9:
Update safety weight 𝜆←𝜆−𝜂𝜆∇𝜆𝐽𝜆(𝜆)
10:
end if
11:
Sample batch tuples (𝑥𝑡, 𝑢𝑡, 𝑟(𝑥𝑡, 𝑢𝑡), 𝑟𝑐(𝑥𝑡, 𝑢𝑡), 𝑥𝑡+1) from 𝐷
12:
Update distributional critic 𝑤𝑖
𝑞←𝑤𝑖
𝑞−𝜂𝑞∇𝑤𝑖𝑞𝐽𝑧(𝑤𝑖
𝑞), 𝑖= 1, 2
13:
Update cost critic 𝑤𝑖
𝑐←𝑤𝑖
𝑐−𝜂𝑐∇𝑤𝑖𝑐𝐽𝑐(𝑤𝑖
𝑐), 𝑖= 1, 2
14:
Update risky policy 𝜃̄𝑢←𝜃̄𝑢+ 𝜂̄𝑢∇𝜃̄𝑢𝐽𝜋̄𝑢(𝜃̄𝑢)
15:
Update safety modulator 𝜃Δ𝑢←𝜃Δ𝑢+ 𝜂Δ𝑢∇𝜃̄𝑢𝐽𝜋Δ𝑢(𝜃Δ𝑢)
16:
Update target networks:
̃𝑤𝑞←(1 −𝜏) ̃𝑤𝑞+ 𝜏𝑤𝑞, ̃𝑤𝑐←(1 −𝜏) ̃𝑤𝑐+ 𝜏𝑤𝑐,
̃𝜃̄𝑢←(1 −𝜏) ̃𝜃̄𝑢+ 𝜏𝜃̄𝑢, ̃𝜃Δ𝑢←(1 −𝜏) ̃𝜃Δ𝑢+ 𝜏𝜃Δ𝑢
17:
𝐦= 𝐦+ 1
18: end while
5.2.  Policy improvement
5.2.1.  Distributional risky policy improvement
The parameter 𝜃̄𝑢 of the risky policy 𝜋𝜃̄𝑢 should be optimized to enhance task performance. According to the decoupled structure 
depicted in Fig. 1, the gradient for 𝜃̄𝑢 originates solely from the reward critic 𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡). Although the critic evaluates the ﬁnal action 
𝑢𝑡, the optimization of 𝜃̄𝑢 proceeds via its inﬂuence on ̄𝑢𝑡. Consequently, the objective for improving the policy becomes to maximize: 
𝐽𝜋̄𝑢(𝜃̄𝑢) = 𝔼[𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)].
It should be noted that the action ̄𝑢𝑡 is sampled from a Gaussian distribution, which is non-diﬀerentiable. Thus, to address this, the 
reparameterization trick is employed. This technique involves sampling from a standard normal distribution and scaling the sample 
by the standard deviation and adding the mean, which can be represented as ̄𝑢𝑡= 𝑓𝜃̄𝑢(𝜍̄𝑢𝑡; 𝑥𝑡) = ̄𝑢𝑡,mean + 𝜍̄𝑢𝑡⊙̄𝑢𝑡,std, where 𝜍̄𝑢𝑡 follows 
a standard normal distribution, ⊙ is the Hadamard product, ̄𝑢𝑡,mean and ̄𝑢𝑡,std are the mean and standard deviation of policy 𝜋𝜃̄𝑢(⋅|𝑥𝑡), 
respectively. Consequently, the corresponding gradient is given by 
∇𝜃̄𝑢𝐽𝜋̄𝑢(𝜃̄𝑢) = 𝔼[∇𝜃̄𝑢𝑓𝜃̄𝑢(𝜍𝑡; 𝑥𝑡)∇̄𝑢𝑡𝑄𝑤𝑞(𝑥𝑡, 𝑢𝑡)].
5.2.2.  Safe modulator policy improvement
Following the purple gradient path depicted in Fig. 1, the safety modulator 𝜋𝜃Δ is updated to enforce safety. Its training objective 
is decoupled from the reward signal and is instead driven by the safety critic 𝑄𝑐,𝑤𝑐 and the penalty for deviating from the risky action, 
𝑑(𝑢𝑡, ̄𝑢𝑡). Therefore, for a given 𝜆, the safety modulator is improved by maximizing the following objective: 
𝐽𝜋Δ𝑢(𝜃Δ) = 𝔼[−𝑑(𝑢𝑡, ̄𝑢𝑡) −𝜆𝑄𝑐,𝑤𝑐(𝑥𝑡, 𝑢𝑡)].
Journal of the Franklin Institute 362 (2025) 108158 
7

## Page 8

Q. Qi et al.
Fig. 2. The Crazyﬂie 2.1 platform in simulation and the real world.
Similar to the reparameterization trick in distributional risky policy improvement and Δ𝑢𝑡= 𝑓𝜃Δ(𝜍̄𝑢𝑡; 𝑥𝑡), one has 
∇𝜃Δ𝐽𝜋Δ𝑢(𝜃Δ) = 𝔼[−∇𝜃Δ𝑑(𝑢𝑡, ̄𝑢𝑡) −𝜆∇𝜃Δ𝑄𝑐,𝑤𝑐(𝑥𝑡, 𝑢𝑡)].
The detailed SMAC algorithm for alleviating risky policy and mitigating overestimation is presented in Algorithm 1.
6.  Experiments
 In this section, we validate the eﬀectiveness and safety of the proposed SMAC algorithms through both physics-based simulations 
and real-world experiments. To facilitate a smooth sim-to-real transfer, we use the Crazyﬂie 2.1 platform for both settings. The 
simulations are conducted in PyBullet [31] with a Crazyﬂie 2.1 model, while the real-world experiments are performed on the 
physical Crazyﬂie 2.1 quadcopter [30], which is a well-known open-source research platform. Fig. 2 illustrates the simulation model 
and the physical platform, along with its key parameters in Table 1. In both environments, the SMAC algorithms are evaluated on 
two challenging tasks: hovering and ﬁgure-8 tracking.
6.1.  Simulation setup
6.1.1.  UAV hovering task
The UAV hovering task has plenty of deployment senarios, such as ﬁlming, delivery and inspection. In the hovering, one of the 
most important request is that keep UAV stable, which implies that UAV’s rotation, roll, pitch and yaw has little movement. Therefore, 
our goal is to get the suitable action 𝑢𝑡 from SMAC algorithm that give the policy to maxmize reward to let UAV go to the desired 
position and give the safe modulator to limit cost to keep the ro, pitch and yaw in the given constraint. The hovering environment 
deﬁnition is as follow.
Observation: The observation state 𝑥𝑡 is a 13-dimensional vector, which contains four parts: the distance between the target 
position and the current position 𝑝𝑡= (𝑝𝑥
𝑡, 𝑝𝑦
𝑡, 𝑝𝑧
𝑡)𝑇, the current velocity 𝑣𝑡= (𝑣𝑥
𝑡, 𝑣𝑦
𝑡, 𝑣𝑧
𝑡)𝑇, the current quaternion 𝑅(𝜚𝑡), where 𝜚𝑡=
(𝜚𝑟
𝑡, 𝜚𝑝
𝑡, 𝜚𝜓
𝑡)𝑇 is the current Euler angle, 𝑅(⋅) is the equation for converting Euler angle to quaternion, utilized to avoid gimbal lock, the 
Euler angular velocity 𝜔𝑡= (𝜔𝑟
𝑡, 𝜔𝑝
𝑡, 𝜔𝜓
𝑡)𝑇.
Action: The action 𝑢𝑡∈[−𝑢max, 𝑢max] is a 4-dimensional vector, which is obtained from the modulation function 𝑚(̄𝑢𝑡, Δ𝑢𝑡), where 
𝑢max is the action bound. Inspired by [28,29], the corresponding actions and modulation function are designed as ̄𝑢𝑡= (𝑎𝑡, 𝜚𝑟𝑐
𝑡, 𝜚𝑝𝑐
𝑡, 𝜚𝜓𝑐
𝑡)𝑇, 
where 𝑎𝑡 is the total acceleration command of the body’s z-axis, 𝜚𝑟𝑐
𝑡, 𝜚𝑝𝑐
𝑡 and 𝜚𝜓𝑐
𝑡 are the roll, pitch and yaw angle commands, 
respectively. Δ𝑢𝑡 is the corresponding safety modulator for ̄𝑢𝑡 and 𝑢𝑡= 𝑚(̄𝑢𝑡, Δ𝑢𝑡) = ̄𝑢𝑡+ Δ𝑢𝑡.
Reward & cost reward design: The reward function contains ﬁve parts: the distance reward 𝑟𝑑𝑖𝑠= −‖𝑝𝑡‖, the velocity 
reward 𝑟𝑣𝑒𝑙= −0.1‖𝑣𝑡‖, the stay reward 𝑟𝑠𝑡𝑎=
{
1.5,
if ‖𝑝𝑡‖ < 0.02,
0,
otherwise,
 the action reward 𝑟𝑎𝑐𝑡= −‖𝑢𝑡‖, and the hit reward 𝑟ℎ𝑖𝑡=
Table 1 
Crazyﬂie 2.1 parameters.
 Parameters
 Values
 Mass
 28 g
 Arm
 3.97 cm
 Propeller radius
 2.31 cm
 Max speed
 30 km/h
 Thrust2weight
 1.88
 Hovering position
(0m, 0m, 1.5m)𝑇
Journal of the Franklin Institute 362 (2025) 108158 
8

## Page 9

Q. Qi et al.
Table 2 
Training parameters.
 Episode steps
 Training steps
 Buﬀer size
 1000
5 × 106
1 × 106
 Target update 𝜏
 Discount factor 𝛾
 Batch size
5 × 10−3
 0.99
 512
 Safety constraint 𝐶
 Learning rate 𝜂
 Start learning step
 50 (hovering)
1 × 10−4
100
 0 (ﬁgure-8 tracking)
{
−1,
if hit the boundary,
0,
otherwise.
 The total reward function is deﬁned as 
𝑟(𝑥𝑡, 𝑢𝑡) = (𝑟𝑑𝑖𝑠+ 𝑟𝑣𝑒𝑙+ 𝑟𝑎𝑐𝑡+ 𝑟ℎ𝑖𝑡+ 𝑟𝑠𝑡𝑎)𝑑𝑡,
(19)
where 𝑑𝑡= 1∕240 is the time step in PyBullet.
The cost reward function is designed to constrain Euler angles, which contains three parts: The roll angle cost reward 𝑟𝑟
𝑐, the pitch 
angle cost reward 𝑟𝑝
𝑐, and the yaw angle cost reward 𝑟𝜓
𝑐, where
𝑟𝑟
𝑐=
{
1,
if‖𝜚𝑟
𝑡‖ < 0.2,
0,
otherwise,
𝑟𝑝
𝑐=
{
1,
if‖𝜚𝑝
𝑡‖ < 0.2,
0,
otherwise,
𝑟𝜓
𝑐=
{
1,
if‖𝜚𝜓
𝑡‖ < 0.2,
0,
otherwise.
The total cost reward function is deﬁned as 
𝑟𝑐(𝑥𝑡, 𝑢𝑡) = 𝑟𝑟
𝑐+ 𝑟𝑝
𝑐+ 𝑟𝜓
𝑐.
(20)
6.1.2.  UAV ﬁgure-8 tracking task
The UAV ﬁgure-8 tracking task represents a fundamental challenge in UAV ﬂight control, with applications in aerial surveillance, 
rescue operations, and autonomous inspection missions. In ﬁgure-8 trajectory tracking, one of the most critical requirements is 
maintaining precise path tracking while ensuring smooth ﬂight dynamics, which implies that the UAV must accurately follow the 
reference trajectory while maintaining stable orientation and avoiding obstacles. Therefore, our goal is to obtain the suitable action 
𝑢𝑡 from SMAC algorithm that provides the policy to maximize reward for UAV trajectory following and applies the safety modulator 
to avoide obstacles. The reference ﬁgure-8 trajectory 𝑝𝑟𝑒𝑓
𝑡 is deﬁned as: 
𝑝𝑟𝑒𝑓
𝑡
=
(
sin
( 2𝜋𝑡
𝑇
)
, sin
( 4𝜋𝑡
𝑇
)
, 1.0
)𝑇
,
where 𝑇= 1000 is the total period steps. Three spherical obstacles with radius 0.1 are positioned at: 
𝑜1 = (1.0, 0.0, 1.0)𝑇,
𝑜2 = (−1.0, 0.0, 1.0)𝑇,
𝑜3 = (0.5, 0.43, 1.0)𝑇.
Observation: The observation state 𝑥𝑡 is a 28-dimensional vector, which contains six parts: the relative positions to future tra-
jectory waypoints 𝑟𝑝𝑜𝑠 (4 waypoints × 3 coordinates), the current quaternion 𝑅(𝜚𝑡), the current velocity 𝑣𝑡, the current Euler angular 
velocity 𝜔𝑡, the heading direction vector ℎ𝑡, and the up direction vector 𝜒𝑡.
Action: The action state is deﬁned similarly to the hovering task. The action 𝑢𝑡 is also a 4-dimensional vector composed of a base 
action ̄𝑢𝑡 and a safety modulation Δ𝑢𝑡. The key diﬀerence is that for this dynamic tracking task, we use a yaw rate command ( ̇𝜓𝑐
𝑡) 
instead of the yaw angle command. The base action ̄𝑢𝑡 is therefore deﬁned as ̄𝑢𝑡= (𝑎𝑡, 𝜚𝑟𝑐
𝑡, 𝜚𝑝𝑐
𝑡, ̇𝜓𝑐
𝑡)𝑇. The modulation function remains 
𝑢𝑡= 𝑚(̄𝑢𝑡, Δ𝑢𝑡) = ̄𝑢𝑡+ Δ𝑢𝑡.
Reward & cost design: The reward function contains four parts: the position tracking reward 𝑟𝑝𝑜𝑠= exp(−1.8 ⋅𝔡𝑡) where 𝔡𝑡=
‖𝑝𝑟𝑒𝑓
𝑡
−𝑝𝑡‖ is the distance to the reference trajectory, the orientation reward 𝑟𝑢𝑝=
0.5
1.0+𝜍2  where 𝜍 measures the deviation from upright 
orientation, the spin penalty 𝑟𝑠𝑝𝑖𝑛=
0.5
1.0+(𝜔𝜓
𝑡)2  to discourage excessive yaw rotation, and the eﬀort reward 𝑟𝑒𝑓𝑓𝑜𝑟𝑡= 0.1𝑎𝑡 to encourage 
eﬃcient control. The total reward function is deﬁned as 
𝑟(𝑥𝑡, 𝑢𝑡) = (𝑟𝑝𝑜𝑠+ 𝑟𝑝𝑜𝑠⋅(𝑟𝑢𝑝+ 𝑟𝑠𝑝𝑖𝑛) + 𝑟𝑒𝑓𝑓𝑜𝑟𝑡)𝑑𝑡
The cost function is designed to enforce obstacle avoidance constraints. For spherical obstacles at positions 𝑜𝑖 with safety collision-free 
distance 𝑟𝑜𝑏𝑠= 0.15, 𝑖= 1, 2, 3, the cost is deﬁned as:
𝑟𝑐(𝑥𝑡, 𝑢𝑡) =
{
1,
if min𝑖‖𝑝𝑡−𝑜𝑖‖ ≤𝑟𝑜𝑏𝑠
0,
otherwise
The total cost function ensures safe navigation through the ﬁgure-8 trajectory while avoiding collisions with spherical obstacles 
positioned along the ﬂight path.
Journal of the Franklin Institute 362 (2025) 108158 
9

## Page 10

Q. Qi et al.
Table 3 
The violation counts of roll, pitch, and yaw.
 Algorithms
 roll
 pitch
 yaw
 total
 SAC
72.80 ± 8.87
74.40 ± 5.41
95.00 ± 4.18
242.20 ± 10.73
 SMAC
20.40 ± 2.70
20.20 ± 1.79
7.20 ± 2.59
47.80 ± 4.44
Fig. 3. The average return training curves of SAC, SAC-Lag, and SMAC by running 5 times. The lines and the shaded area represent the average 
return and the 95 % conﬁdence interval, respectively.
Fig. 4. The average cost training curves of SAC, SAC-Lag, and SMAC by running 5 times. The red dashed line indicates the safety constraint threshold, 
set to 𝐶= 50 and 𝐶= 0 for subﬁgures (a) and (b), respectively. (For interpretation of the references to colour in this ﬁgure legend, the reader is 
referred to the web version of this article.)
Fig. 5. The true average Q-value (solid lines) and estimated average Q-value (dashed lines) training curves by running 5 times at the 500th step 
per episode.
Journal of the Franklin Institute 362 (2025) 108158 
10

## Page 11

Q. Qi et al.
Fig. 6. The Crazyﬂie 2.1 hovering at 1.5m height in real-world.
Fig. 7. The roll, pitch, and yaw curves during hovering task using SAC (a) and SMAC (b).
6.2.  Training results
Before training, the risky policy, safety modulator, distributional critic, and cost critic networks are all modeled as 2-layer percep-
trons with 256 hidden units. The activation function used in each unit is ReLU, and the ﬁnal outputs of all networks are linear. The 
SMAC algorithm is designed on the Stable Baselines3. The training is conducted on a computer with an i7-13700K CPU and rendered 
with an RTX 4060ti GPU. The detailed training parameters are shown in Table 2.
Two model-free methods are introduced to compare with SMAC algorithm, which are SAC [21] and SAC-Lag [22]. The simulation 
results of average return are shown in Fig. 3. The proposed SMAC makes the higher average return in both hovering and ﬁgure-8 
tracking tasks compare with SAC and SAC-Lag algorithm. For hovering task, safety constraint is 50 and safety constraint ia 0 in the 
ﬁgure-8 tracking task.
As shown in Fig. 4a, the Number of attitude angle constraint violations are declined through training steps, however, only SMAC 
achieves convergence with violation number less than 50. In Fig. 4b, only SMAC learns no collision with obstacles in the ﬁgure-8 
tracking with the help of safety modulator, notably, the average cost is 0 at initial training step because UAV haven’t learn how to 
tracking the ﬁgure-8 trajectory and ﬂy random therefore they won’t touch the obstacle on the trajectory, makes the cost 0 at initial 
training step.
To evaluate the eﬀect of Q-value overestimation mitigation with distributional critic, we record the true Q-value and estimated 
Q-value by running ﬁve times with diﬀerent seeds in hovering and ﬁgure-8 tracking tasks. Fig. 5 shows the true Q-value and estimated 
Journal of the Franklin Institute 362 (2025) 108158 
11

## Page 12

Q. Qi et al.
Fig. 8. The Crazyﬂie 2.1 tracking a ﬁgure-8 trajectory and avoiding black spherical obstacles in the real world.
Fig. 9. The actual ﬂight path for Crazyﬂie 2.1 compared against the reference ﬁgure-8 trajectory, demonstrating successful obstacle avoidance.
Q-value curves during training. The Q-value is calculated once at the 500th steps per episode. In Fig. 5a, the estimated Q-value of 
SAC-Lag has severe estimation ﬂuctuations because the policy fails to trade oﬀ the maximization of rewards against cost rewards, 
resulting in severe ﬂuctuations in the Q-value estimation. Compared to SAC and SAC-Lag, SMAC exhibits a lower overestimation bias 
when convergence, indicating that the distributional critic eﬀectively mitigates overestimation.
Journal of the Franklin Institute 362 (2025) 108158 
12

## Page 13

Q. Qi et al.
6.3.  Real-world experiment
With the help of precise simulation models of PyBullet, the UAV hovering and ﬁgure-8 tracking tasks can be easily deployed to 
the Crazyﬂie 2.1 in real-world as shown in Figs. 6 and 8. In real-world experiments, position and orientation information, such as 
Euler angles, are primarily calculated based on NOKOV Motion Capture System.
As shown in Fig. 7, compared with SAC, the Crazyﬂie 2.1 controlled by the SMAC algorithm not only completes the hovering 
task but also exhibits smaller ﬂuctuations in the Euler angles, essentially meeting the safety constraints. After 5 rounds of testing, the 
violation counts of the safety constraints by SMAC and SAC on the real-world device are presented in Table 3. Regarding the total 
violation counts for roll, pitch, and yaw under safety constraints with 𝐶= 50, with the help of the safety modulator, SMAC achieves 
safety constraints with a signiﬁcantly smaller average total violation count of 47.80. In contrast, SAC exhibits a substantially higher 
average count of 242.20. Moreover, as for ﬁgure-8 tracking task, SMAC algorithm achieves collision-free tracking as shown in Fig. 9. 
Moreover, for the challenging ﬁgure-8 tracking task, the SMAC algorithm demonstrated exceptional performance. As visualized in 
Fig. 9, the UAV successfully executed a collision-free trajectory, closely following the reference path while adeptly avoiding all three 
spherical obstacles.
Overall, Figs. 3–9 eﬀectively demonstrate that the SMAC algorithm not only maintains its safety guarantees but also achieves a 
high performance in the simulation and real-world scenario.
7.  Conclusions
 In this paper, a novel SMAC approach is proposed to address the issues of both safety and overestimation in safe RL, where 
the safety modulator allows the policy to concentrate on maximizing rewards without the burden of trading oﬀ safety constraints. 
By introducing the theoretical update rule, the distributional critic can eﬀectively mitigates overestimation. Both simulations and 
real-world scenarios demonstrate that the proposed SMAC strategy for UAV hovering and ﬁgure-8 tracking tasks can maintain safety 
constraints and signiﬁcantly outperforms existing baseline algorithms. This work paves the way for safer and more reliable deployment 
of model-free safe RL agents in real-world applications.
CRediT authorship contribution statement
Qihan Qi: Writing – original draft, Investigation, Formal analysis; Xinsong Yang: Writing – review & editing, Supervision, Method-
ology, Funding acquisition; Daniel W C Ho: Writing – review & editing, Validation, Resources; Yaping Sun: Writing – review & 
editing, Validation, Formal analysis.
Contribution
1. A model-free safety modulator is presented to modulate the action of policy, which enables the policy to neglect cost rewards 
and focus on maximizing rewards. Without the safety modulator, the policies in the literature may suﬀer failures in the learning 
process because they always need to trade oﬀ the maximization of rewards against cost rewards.
2. To mitigate overestimation, a distributional critic for SMAC is proposed to incorporate distributional information with theoreti-
cally updated rules to mitigate overestimation under safety constraints. Diﬀerent from existing papers, the overestimation mitigation 
approach is given by detailed theoretical analysis.
3. Both PyBullet simulations and real-world experiments for UAV hovering demonstrate that the proposed SMAC algorithm can 
eﬀectively mitigate overestimation while maintaining safety constraints. Comparative experiments show the merit that our algorithm 
outperforms the mainstream baseline algorithms in the references.
Declaration of competing interest
We declare that we have no ﬁnancial and personal relationships with other people or organizations that can inappropriately 
inﬂuence our work, there is no professional or other personal interest of any nature or kind in any product, service and/or company 
that could be construed as inﬂuencing the position presented in, or the review of, the manuscript entitled “Safety Modulator Actor-
Critic Method in Model-Free Safe Reinforcement Learning and Application in UAV Hovering”. 
Acknowledgment
This work was supported in part by the National Natural Science Foundation of China (NSFC) under Grant Nos. 62373262 and 
62303336, and in part by the National Funded Postdoctoral Researcher Program of China under Grant GZB20230467, and in part 
by the China Postdoctoral Science Foundation under Grant 2023M742457, and in part by the Fund of Robot Technology Used for 
Special Environment Key Laboratory of Sichuan Province under Grant No. 24kftk01, and in part by the Research Grants Council of 
Hong Kong Special Administrative Region under Grant Nos. GRF (CityU 11205724 and CityU 11306825).
Journal of the Franklin Institute 362 (2025) 108158 
13

## Page 14

Q. Qi et al.
References
[1] D. Silver, A. Huang, C.J. Maddison, Mastering the game of go with deep neural networks and tree search, Nature 529 (7587) (2016) 484–489.
[2] S. Yang, L. Jin, J. Rao, Reinforcement learning based attitude fault-tolerant control of spacecraft with unknown system model, J. Franklin Inst. 362 (10) (2025) 
107741.
[3] N. Zheng, J. Liu, L. Su, S. Lv, H. Shen, Output synchronization of a class of complex dynamic networks: a reinforcement learning method, J. Franklin Inst. 361 
(17) (2024) 107284.
[4] T. Zhang, D. Wu, A.S. Yamashita, A fault reconﬁguration strategy based on logical structure and improved reinforcement learning for ship DC regional grid, J. 
Franklin Inst. 361 (15) (2024) 107111.
[5] J. Hao, T. Yang, H. Tang, C. Bai, J. Liu, Z. Meng, Exploration in deep reinforcement learning: from single-agent to multiagent domain, IEEE Trans. Neural Netw. 
Learn. Syst. 35 (7) (2024) 8762–8782.
[6] X. Gao, J. Si, H. Huang, Reinforcement learning control with knowledge shaping, IEEE Trans. Neural Netw. Learn. Syst. 35 (3) (2024) 3156–3167.
[7] Y. Liu, Y. Gao, Q. Zhang, D. Ding, D. Zhao, Multi-task safe reinforcement learning for navigating intersections in dense traﬃc, J. Franklin Inst. 360 (17) (2023) 
13737–13760.
[8] A. Mehrjouyan, M.B. Menhaj, A. Hooshiar, Adaptive-neural command ﬁltered synchronization control of tele-robotic systems using disturbance observer with 
safety enhancement, J. Franklin Inst. 361 (13) (2024) 107036.
[9] K.P. Wabersich, A.J. Taylor, J.J. Choi, K. Sreenath, C.J. Tomlin, A.D. Ames, M. Zeilinger, Data-driven safety ﬁlters: Hamilton-Jacobi reachability, control barrier 
functions, and predictive methods for uncertain systems, IEEE Control Syst. Mag. 43 (5) (2023) 137–177.
[10] J. Bai, L. Jia, Z. Peng, A new insight on augmented Lagrangian method with applications in machine learning, J. Sci. Comput. 99 (2) (2024) 53–59.
[11] C.A. Cheng, H.P. Huang, Learn the Lagrangian: a vector-valued RKHS approach to identifying Lagrangian systems, IEEE Trans. Cybern. 46 (12) (2015) 3247–3258.
[12] A. Modares, N. Sadati, B. Esmaeili, Safe reinforcement learning via a model-free safety certiﬁer, IEEE Trans. Neural Netw. Learn. Syst. 35 (3) (2024) 3302–3311.
[13] J. Wu, Z. Jin, A. Liu, L. Yu, F. Yang, A survey of learning-based control of robotic visual servoing systems, J. Franklin Inst. 359 (1) (2022) 556–577.
[14] Z. Zhang, H. Tao, Y. Chen, T. Oomen, W. Paszke, E. Rogers, Optimal iterative learning control design for continuous-time systems with nonidentical trial lengths 
using alternating projections between multiple sets, J. Franklin Inst. 360 (5) (2023) 3825–3848.
[15] H.V. Hasselt, A. Guez, D. Silver, Deep reinforcement learning with double Q-learning, Proc. AAAI Conf. Artif. Intell. 30 (2016).
[16] X. Liu, P. Huang, S.S. Ge, Optimized control for human-multi-robot collaborative manipulation via multi-player Q-learning, J. Franklin Inst. 358 (11) (2021) 
5639–5658.
[17] J. Duan, Y. Guan, S.E. Li, Distributional soft actor-critic: oﬀ-policy reinforcement learning for addressing value estimation errors, IEEE Trans. Neural Netw. 
Learn. Syst. 33 (11) (2021) 6584–6598.
[18] H. Hasselt, Double Q-learning, Adv. Neural Inf. Process. Syst. 23 (2010).
[19] J. Li, Y. Li, Q. Su, Sequential recovery of cyber-physical power systems based on improved Q-learning, J. Franklin Inst. 360 (17) (2023) 13692–13711.
[20] B. Du, W. Xie, Y. Li, Q. Yang, W. Zhang, R.R. Negenborn, Safe adaptive policy transfer reinforcement learning for distributed multiagent control, IEEE Trans. 
Neural Netw. Learn. Syst. 36 (1) (2025) 1939–1946.
[21] X. Wang, D. Li, Bioinspired actor-critic algorithm for reinforcement learning interpretation with Levy-Brown hybrid exploration strategy, Neurocomputing 574 
(2024) 127291.
[22] I. Radosavovic, T. Xiao, B. Zhang, T. Darrell, J. Malik, K. Sreenath, Real-world humanoid locomotion with reinforcement learning, Sci. Robot 9 (89) (2024) 
9579.
[23] D. Zhu, Q. Zhu, Stabilization of stochastic nonlinear semi-Markov jump systems via aperiodic intermittent feedback control, J. Franklin Inst. 362 (10) (2025) 
107749.
[24] Y. Huang, W. Li, Y. Wang, H. Shen, Optimal control for continuous-time Markov jump singularly perturbed systems: a hybrid reinforcement learning scheme, J. 
Franklin Inst. 361 (7) (2024) 106771.
[25] R. Munos, T. Stepleton, A. Harutyunyan, Safe and eﬃcient oﬀ-policy reinforcement learning, Adv. Neural Inf. Process. Syst. 29 (2016).
[26] H. Xu, J. Xuan, G. Zhang, J. Lu, Trust region policy optimization via entropy regularization for Kullback-Leibler divergence constraint, Neurocomputing 589 
(2024) 127716.
[27] L. Zou, H. Wu, R. Liu, C. Yi, J. He, Y. Li, A new method for LDPC blind recognition over a candidate set using Kullback-Leibler divergence, IEEE Commun. Lett. 
28 (5) (2024) 964–968.
[28] H. Yu, W. Xu, H. Zhang, Towards safe reinforcement learning with a safety editor policy, Adv. Neural Inf. Process. Syst. 35 (2022) 2608–2621.
[29] Y. Feng, T. Yang, Y. Yu, P. Enhancing, UAV aerial docking: a hybrid approach combining oﬄine and online reinforcement learning, Drones 8 (5) (2024) 168.
[30] W. Giernacki, M. Skwierczyski, W. Witwicki, P. Wroski, P. Kozierski, Crazyﬂie 2.0 quadrotor as a platform for research and education in robotics and control 
engineering, in: 22nd International Conference on Methods and Models in Automation and Robotics (MMAR), IEEE, 2017, pp. 37–42.
[31] E. Coumans, Y. Bai, PyBullet Quickstart Guide, 2021. https://docs.google.com/document/u/1/d.
Journal of the Franklin Institute 362 (2025) 108158 
14
