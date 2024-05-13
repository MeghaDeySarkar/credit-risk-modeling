# Prioritizing Loan Approval Decisions using Credit Risk Modelling

# Problem Statement:
# The objective is to develop a credit risk model that prioritizes loan approval decisions by assigning priority levels (P1, P2, P3, P4) 
# to customers based on their creditworthiness. The priority levels indicate the likelihood of default and help in determining whether a loan should be granted.

# Banking
# Asset -> loan products, credit cards. something that gives profit
# Liability -> {current account, savings acc (CASA)}, {fixed deposit, RD (Term deposits)}

# Disbursed amount -> loan amount given to a customer
# OSP -> outstanding principle (becomes 0 at the end of loan cycle)
# Amortization
# DPD -> Days past due (Ideally should be 0 days)
# PAR -> Portfolio at risk. OSP when DPD > 0 days
# NPA -> # NPA -> non performing asset (Loan that is defaulted). Loan account when DPD > 90 days

# Credit Risk types in banking
# DPD (0 days) -> NDA (Non delinquit account) -> no default sccount -> Timely payments made
# DPD (0 to 30 days) -> SMA1 (Standard Monitoring Account)
# DPD (30 to 60 days) -> SMA2 (Standard Monitoring Account)
# DPD (60 to 90 days) -> SMA3 (Standard Monitoring Account)
# DPD (90 to 180 days) -> NPA
# DPD (>180) -> Written-off (Loan which is not present) -> to improve NPA -> Loan portfolio the the bank becomes better -> improves stock price

# NPA has 2 parts
# GNPA -> Gross NPA (3-5)% of the OSP is at default
# NNPA -> Net NPA -> (0.01 to 0.06)% -> Provisioning amount subtracted from the defaulted account by th bank itself
# Bank quality assessment -> GNPS value

# Trade-Line -> Loan (secured or unsecured)

# Team structure for a DS project
# Data science -> MLOPS -> Data Engineering (extraxt, transform, load) -> Business Team -> Distribution Team