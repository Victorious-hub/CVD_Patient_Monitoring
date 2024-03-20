package com.example.cvd_monitoring.domain.use_case.doctor_update

import com.example.cvd_monitoring.domain.model.users.DoctorContact
import com.example.cvd_monitoring.domain.model.users.PatientContact
import com.example.cvd_monitoring.domain.model.users.UserContact
import com.example.cvd_monitoring.domain.repository.PatientRepository
import javax.inject.Inject

class DoctorContactUseCase @Inject constructor(
    private val patientRepository: PatientRepository
) {
    suspend operator fun invoke(firstName: String, lastName: String, email: String, slug: String): DoctorContact {
        val user = UserContact(firstName, lastName, email)
        return patientRepository.updateDoctorContact(DoctorContact(user), slug)
    }
}


