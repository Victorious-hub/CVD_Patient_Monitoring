package com.example.cvd_monitoring.domain.model.users

data class Doctor(
    val patients: List<Patient>,
    val patient_cards: List<Patient>,
    val user: User,
    val slug: String
)
