class FakeSession:

    should_commit_fail = True
    rollback_called = False

    def commit(self):
        if self.should_commit_fail:
            raise Exception("Commit failed")

        print("commit called")

    def rollback(self):
        self.rollback_called = True
        print("rollback called")
        pass