package com.example.cvd_monitoring.presentation

sealed class Screen(val route: String) {
    data object Home : Screen("home")
    data object SignUp : Screen("signUp")
    data object  SignIn : Screen("SignIn")
    data object  UpdateDataPatient : Screen("updateData")
    data object  UpdateContactPatient : Screen("updateContactPatient")
    data object  UpdateContactDoctor : Screen("UpdateContactDoctor")
    data object  PatientList : Screen("patientList")
}