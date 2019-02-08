
""" Reservation settings controller."""
from timeless.reservations.models import ReservationSettings


class SettingsController:
    """
      @todo #63:30min Continue implementing SettingsController:
       CRUD operations should be implemented, as well as unit tests
       and integration tests.
    """

    def get_settings_for_reservation(self, reservation_id) -> ReservationSettings:
        raise Exception(
            "SettingsController#get_settings_for_reservation not yet implemented"
        )

    def get_all_reservation_settings(self):
        raise Exception(
            "SettingsController#get_all_reservation_settings not yet implemented"
        )

    def create_settings_for_reservation(self, settings) -> ReservationSettings:
        raise Exception(
            "SettingsController#create_reservation_settings not yet implemented"
        )

    def update_reservation_settings(self, reservation_id, new_settings):
        raise Exception(
            "SettingsController#update_reservation_settings not yet implemented"
        )

    def delete_reservation_settings(self, reservation_id):
        raise Exception(
            "SettingsController#delete_reservation_settings not yet implemented"
        )
