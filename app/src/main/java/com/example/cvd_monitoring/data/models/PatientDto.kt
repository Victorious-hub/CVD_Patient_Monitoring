package com.example.cvd_monitoring.data.models


import com.example.cvd_monitoring.domain.model.users.Patient
import com.example.cvd_monitoring.domain.model.users.User
import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class PatientDto(
    @Json(name = "age")
    val age: Int,
    @Json(name = "birthday")
    val birthday: String,
    @Json(name = "gender")
    val gender: String,
    @Json(name = "height")
    val height: Int,
    @Json(name = "slug")
    val slug: String,
    @Json(name = "user")
    val user: User,
    @Json(name = "weight")
    val weight: Double
)

fun PatientDto.toPatient(): Patient {
    return Patient(
        age = age,
        birthday = birthday,
        gender = gender,
        height = height,
        slug = slug,
        user = user,
        weight = weight
    )
}