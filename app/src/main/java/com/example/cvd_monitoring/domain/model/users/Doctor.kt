package com.example.cvd_monitoring.domain.model.users

data class Doctor(
    val patients: List<Patient>,
    val user: User
)
