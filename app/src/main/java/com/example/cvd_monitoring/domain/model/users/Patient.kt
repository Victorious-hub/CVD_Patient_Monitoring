package com.example.cvd_monitoring.domain.model.users

data class Patient(
    val age: Int,
    val birthday: String,
    val gender: String,
    val height: Int,
    val slug: String,
    val mobile: String,
    val user: User,
    val weight: Double
)